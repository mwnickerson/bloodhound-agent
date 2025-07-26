import json
from typing import Any, Dict, List

import requests

from .base import BloodhoundBaseClient, BloodhoundAPIError, BloodhoundConnectionError


class CypherClient:
    """Client for Cypher query related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def run_query(self, query: str, include_properties: bool = True) -> Dict[str, Any]:
        """
        Run a custom Cypher query directly against the database

        Args:
            query: The Cypher query to execute
            include_properties: Whether to include node/edge properties in response

        Returns:
            Dictionary with graph data (nodes and edges) and metadata about the query result

        Raises:
            BloodhoundAPIError: For authentication, server errors, or malformed queries
            BloodhoundConnectionError: For network connectivity issues

        Note: 404 responses are treated as successful queries with no results, not errors
        """
        data = {"query": query, "includeproperties": include_properties}

        try:
            response = self.base_client._request(
                "POST", "/api/v2/graphs/cypher", json.dumps(data).encode("utf8")
            )

            if response.status_code == 200:
                try:
                    json_data = response.json()
                    return {
                        "success": True,
                        "data": json_data.get("data", {}),
                        "metadata": {
                            "status": "success_with_results",
                            "query": query,
                            "has_results": True,
                            "status_code": 200,
                        },
                    }
                except json.JSONDecodeError:
                    raise BloodhoundAPIError(
                        "Invalid JSON response from Cypher query", response=response
                    )

            elif response.status_code == 404:
                return {
                    "success": True,
                    "data": {"nodes": [], "edges": []},
                    "metadata": {
                        "status": "success_no_results",
                        "query": query,
                        "has_results": False,
                        "status_code": 404,
                        "message": "Query executed successfully but found no matching data",
                    },
                }

            elif response.status_code == 400:
                try:
                    error_data = response.json()
                    error_detail = error_data.get("error", "Unknown syntax error")
                except json.JSONDecodeError:
                    error_detail = "Malformed Cypher query"

                raise BloodhoundAPIError(
                    f"Cypher query syntax error: {error_detail}", response=response
                )

            elif response.status_code == 401:
                raise BloodhoundAPIError(
                    "Authentication failed - check your BloodHound API credentials",
                    response=response,
                )

            elif response.status_code == 403:
                raise BloodhoundAPIError(
                    "Permission denied - insufficient privileges for Cypher queries",
                    response=response,
                )

            elif response.status_code == 429:
                raise BloodhoundAPIError(
                    "Rate limit exceeded - too many requests. Please wait before retrying.",
                    response=response,
                )

            elif response.status_code >= 500:
                try:
                    error_data = response.json()
                    error_detail = error_data.get("error", "Unknown server error")
                except json.JSONDecodeError:
                    error_detail = f"HTTP {response.status_code}"

                raise BloodhoundAPIError(
                    f"BloodHound server error: {error_detail}", response=response
                )

            else:
                raise BloodhoundAPIError(
                    f"Unexpected response status: {response.status_code}",
                    response=response,
                )

        except requests.exceptions.ConnectionError as e:
            raise BloodhoundConnectionError(
                f"Failed to connect to BloodHound for Cypher query: {e}"
            )
        except requests.exceptions.Timeout as e:
            raise BloodhoundConnectionError(f"Request timeout during Cypher query: {e}")
        except requests.exceptions.RequestException as e:
            raise BloodhoundConnectionError(f"Network error during Cypher query: {e}")

    def run_query_with_retry(
        self, query: str, include_properties: bool = True, max_retries: int = 3
    ) -> Dict[str, Any]:
        """
        Run a Cypher query with automatic retry logic for transient failures

        Args:
            query: The Cypher query to execute
            include_properties: Whether to include node/edge properties
            max_retries: Maximum number of retry attempts

        Returns:
            Query result dictionary

        Raises:
            BloodhoundAPIError: For non-retryable errors (syntax, auth, permissions)
            BloodhoundConnectionError: For persistent connection issues
        """
        import time

        last_exception = None

        for attempt in range(max_retries + 1):
            try:
                return self.run_query(query, include_properties)

            except BloodhoundConnectionError as e:
                last_exception = e
                if attempt < max_retries:
                    wait_time = 2**attempt  # Exponential backoff: 2, 4, 8 seconds
                    time.sleep(wait_time)
                    continue
                else:
                    raise

            except BloodhoundAPIError as e:
                # Don't retry client errors (4xx) except rate limiting
                if e.status_code in [400, 401, 403]:
                    raise

                # Retry rate limiting and server errors
                last_exception = e
                if attempt < max_retries and (
                    e.status_code == 429 or e.status_code >= 500
                ):
                    wait_time = 2**attempt
                    if e.status_code == 429:
                        wait_time = max(
                            wait_time, 10
                        )  # Minimum 10 seconds for rate limiting
                    time.sleep(wait_time)
                    continue
                else:
                    raise

        raise last_exception

    def validate_query(self, query: str) -> Dict[str, Any]:
        """
        Validate a Cypher query without executing it

        Args:
            query: The Cypher query to validate

        Returns:
            Dictionary with validation results
        """
        basic_checks = {
            "is_empty": not query.strip(),
            "has_return": "RETURN" in query.upper(),
            "has_match": "MATCH" in query.upper(),
            "estimated_complexity": "high"
            if any(keyword in query.upper() for keyword in ["*", "ALL", "COLLECT"])
            else "medium",
        }

        return {
            "valid": not basic_checks["is_empty"],
            "checks": basic_checks,
            "warnings": [
                "Query appears empty" if basic_checks["is_empty"] else None,
                "Query may have high complexity"
                if basic_checks["estimated_complexity"] == "high"
                else None,
            ],
        }

    def list_saved_queries(
        self,
        skip: int = 0,
        limit: int = 100,
        sort_by: str = None,
        name: str = None,
        query: str = None,
        user_id: str = None,
        scope: str = None,
    ) -> Dict[str, Any]:
        """
        List saved Cypher queries with optional filtering

        Args:
            skip: Number of results to skip for pagination
            limit: Maximum number of results to return
            sort_by: Field to sort by
            name: Filter by query name
            query: Filter by query content
            user_id: Filter by user ID
            scope: Filter by scope

        Returns:
            Dictionary with saved queries list and metadata
        """
        params = {"skip": skip, "limit": limit}

        if sort_by:
            params["sortby"] = sort_by
        if name:
            params["name"] = name
        if query:
            params["query"] = query
        if user_id:
            params["userid"] = user_id
        if scope:
            params["scope"] = scope

        return self.base_client.request("GET", "/api/v2/saved-queries", params=params)

    def get_saved_query(self, query_id: int) -> Dict[str, Any]:
        """
        Get a specific saved query by ID

        Args:
            query_id: ID of the saved query

        Returns:
            Dictionary with saved query details
        """
        return self.base_client.request("GET", f"/api/v2/saved-queries/{query_id}")

    def create_saved_query(
        self, name: str, query: str, description: str = None
    ) -> Dict[str, Any]:
        """
        Create a new saved Cypher query

        Args:
            name: Name for the saved query
            query: The Cypher query to save
            description: Optional description

        Returns:
            Dictionary with created saved query
        """
        data = {"name": name, "query": query}
        if description:
            data["description"] = description
        return self.base_client.request("POST", "/api/v2/saved-queries", data=data)

    def update_saved_query(
        self,
        query_id: int,
        name: str = None,
        query: str = None,
        description: str = None,
    ) -> Dict[str, Any]:
        """
        Update an existing saved query

        Args:
            query_id: ID of the saved query to update
            name: New name for the query (optional)
            query: New query string (optional)
            description: New description (optional)

        Returns:
            Dictionary with the updated saved query
        """
        data = {}
        if name:
            data["name"] = name
        if query:
            data["query"] = query
        if description:
            data["description"] = description

        return self.base_client.request(
            "PUT", f"/api/v2/saved-queries/{query_id}", data=data
        )

    def delete_saved_query(self, query_id: int) -> None:
        """
        Delete a saved query

        Args:
            query_id: ID of the saved query to delete
        """
        self.base_client.request("DELETE", f"/api/v2/saved-queries/{query_id}")

    def share_saved_query(
        self, query_id: int, user_ids: List[str] = None, public: bool = False
    ) -> Dict[str, Any]:
        """
        Share a saved query with users or make it public

        Args:
            query_id: ID of the saved query to share
            user_ids: List of user IDs to share with
            public: Whether to make the query public

        Returns:
            Dictionary with sharing information
        """
        data = {"public": public}
        if user_ids:
            data["userids"] = user_ids

        return self.base_client.request(
            "PUT", f"/api/v2/saved-queries/{query_id}/permissions", data=data
        )

    def delete_saved_query_permissions(
        self, query_id: int, user_ids: List[str]
    ) -> None:
        """
        Revoke saved query permissions from users

        Args:
            query_id: ID of the saved query
            user_ids: List of user IDs to revoke access from
        """
        data = {"userids": user_ids}
        self.base_client.request(
            "DELETE", f"/api/v2/saved-queries/{query_id}/permissions", data=data
        )