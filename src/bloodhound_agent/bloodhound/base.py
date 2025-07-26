import base64
import datetime
import hashlib
import hmac
import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

import requests

try:
    from dotenv import load_dotenv
    # Try to load environment variables from .env file if dotenv is available
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
except ImportError:
    # dotenv not available, skip loading .env file
    pass


class BloodhoundError(Exception):
    """Custom exception for BloodHound API errors"""

    pass


class BloodhoundAuthError(BloodhoundError):
    """Custom exception for BloodHound authentication errors"""

    pass


class BloodhoundConnectionError(BloodhoundError):
    """Custom exception for BloodHound connection errors"""

    pass


class BloodhoundAPIError(BloodhoundError):
    """Custom exception for BloodHound API errors"""

    def __init__(self, message: str, response: requests.Response):
        super().__init__(message)
        self.response = response
        self.status_code = response.status_code if response else None


class BloodhoundBaseClient:
    def __init__(
        self,
        domain: str = None,
        token_id: str = None,
        token_key: str = None,
        port: int = 443,
        scheme: str = "https",
    ):
        """
        Initialize BloodHound API base client

        Args:
            domain: BloodHound Enterprise domain (e.g. xyz.bloodhoundenterprise.io)
            token_id: API token ID
            token_key: API token key
            port: API port (default: 443)
            scheme: URL scheme (default: https)
        """
        # Load from parameters or environment variables
        self.scheme = scheme
        self.domain = domain or os.getenv("BLOODHOUND_DOMAIN")
        self.port = port
        self.token_id = token_id or os.getenv("BLOODHOUND_TOKEN_ID")
        self.token_key = token_key or os.getenv("BLOODHOUND_TOKEN_KEY")

        # Validate required fields
        if not self.domain:
            raise BloodhoundAuthError(
                "BloodHound domain must be provided either directly or via BLOODHOUND_DOMAIN environment variable"
            )
        if not self.token_id:
            raise BloodhoundAuthError(
                "API token ID must be provided either directly or via BLOODHOUND_TOKEN_ID environment variable"
            )
        if not self.token_key:
            raise BloodhoundAuthError(
                "API token key must be provided either directly or via BLOODHOUND_TOKEN_KEY environment variable"
            )

    def _format_url(self, uri: str) -> str:
        """Format the complete URL from the URI path"""
        formatted_uri = uri
        if uri.startswith("/"):
            formatted_uri = formatted_uri[1:]

        return f"{self.scheme}://{self.domain}:{self.port}/{formatted_uri}"

    def _request(
        self, method: str, uri: str, body: Optional[bytes] = None
    ) -> requests.Response:
        """
        Make a signed request to the BloodHound API

        Args:
            method: HTTP method (GET, POST, etc.)
            uri: Request URI
            body: Optional request body

        Returns:
            Response from the API
        """
        # Digester is initialized with HMAC-SHA-256 using the token key as the HMAC digest key
        digester = hmac.new(self.token_key.encode(), None, hashlib.sha256)

        # OperationKey - first link in signature chain (method + URI)
        digester.update(f"{method}{uri}".encode())

        # Update digester for further chaining
        digester = hmac.new(digester.digest(), None, hashlib.sha256)

        # DateKey - next link in signature chain (RFC3339 datetime to hour)
        datetime_formatted = datetime.datetime.now().astimezone().isoformat("T")
        digester.update(datetime_formatted[:13].encode())

        # Update digester for further chaining
        digester = hmac.new(digester.digest(), None, hashlib.sha256)

        # Body signing - last link in signature chain
        if body is not None:
            digester.update(body)

        # Make the request with signed headers
        try:
            return requests.request(
                method=method,
                url=self._format_url(uri),
                headers={
                    "User-Agent": "bloodhound-api-client 0.1",
                    "Authorization": f"bhesignature {self.token_id}",
                    "RequestDate": datetime_formatted,
                    "Signature": base64.b64encode(digester.digest()),
                    "Content-Type": "application/json",
                },
                data=body,
            )
        except requests.exceptions.ConnectionError as e:
            raise BloodhoundConnectionError(f"Failed to connect to BloodHound API: {e}")

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an API request and return the parsed JSON response

        Args:
            method: HTTP method (GET, POST, etc.)
            uri: Request URI
            params: Optional query parameters
            data: Optional request body data (will be JSON encoded)

        Returns:
            Parsed JSON response
        """
        # Add query parameters if provided
        if params:
            param_strings = []
            for key, value in params.items():
                param_strings.append(f"{key}={value}")
            uri = f"{uri}?{'&'.join(param_strings)}"

        # Prepare request body if provided
        body = None
        if data:
            body = json.dumps(data).encode("utf8")

        # Make the request
        response = self._request(method, uri, body)

        # Handle response
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP Error: {e}"
            try:
                error_data = response.json()
                if "error" in error_data:
                    error_msg = f"{error_msg} - {error_data['error']}"
            except:
                pass
            raise BloodhoundAPIError(error_msg, response=response)
        except json.JSONDecodeError:
            raise BloodhoundAPIError("Invalid JSON response", response=response)