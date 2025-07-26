from typing import Any, Dict

from .base import BloodhoundBaseClient
from .domains import DomainClient
from .users import UserClient
from .groups import GroupClient
from .computers import ComputerClient
from .ous import OUsClient
from .gpos import GPOsClient
from .graph import GraphClient
from .adcs import ADCSClient
from .cypher import CypherClient


class BloodhoundAPI:
    """
    BloodHound API Client

    Provides access to BloodHound API endpoints through resource-specific clients.
    """

    def __init__(
        self,
        domain: str = None,
        token_id: str = None,
        token_key: str = None,
        port: int = 443,
        scheme: str = "https",
    ):
        """
        Initialize BloodHound API client

        Args:
            domain: BloodHound Enterprise domain (e.g. xyz.bloodhoundenterprise.io)
            token_id: API token ID
            token_key: API token key
            port: API port (default: 443)
            scheme: URL scheme (default: https)

        If domain, token_id, or token_key are not provided, they will be loaded from
        environment variables: BLOODHOUND_DOMAIN, BLOODHOUND_TOKEN_ID, BLOODHOUND_TOKEN_KEY
        """
        # Initialize base client
        self.base_client = BloodhoundBaseClient(
            domain, token_id, token_key, port, scheme
        )

        # Initialize resource clients
        self.domains = DomainClient(self.base_client)
        self.users = UserClient(self.base_client)
        self.groups = GroupClient(self.base_client)
        self.computers = ComputerClient(self.base_client)
        self.ous = OUsClient(self.base_client)
        self.gpos = GPOsClient(self.base_client)
        self.graph = GraphClient(self.base_client)
        self.adcs = ADCSClient(self.base_client)
        self.cypher = CypherClient(self.base_client)

    def test_connection(self) -> Dict[str, Any]:
        """
        Test connection to the BloodHound API

        Returns:
            API version information
        """
        try:
            response = self.base_client.request("GET", "/api/version")
            return response["data"]
        except Exception as e:
            print(f"Connection test failed: {e}")
            return None

    def get_self_info(self) -> Dict[str, Any]:
        """
        Get information about the authenticated user

        Returns:
            User information dictionary
        """
        try:
            return self.base_client.request("GET", "/api/v2/self")
        except Exception as e:
            print(f"Failed to get user info: {e}")
            return None