from typing import Any, Dict

from .base import BloodhoundBaseClient


class OUsClient:
    """Client for OU related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_info(self, ou_id: str) -> Dict[str, Any]:
        """
        Get information about a specific OU
        Args:
            ou_id: The ID of the OU to query
        Returns:
            OU information dictionary
        """
        params = {"counts": "true"}
        return self.base_client.request("GET", f"/api/v2/ous/{ou_id}", params=params)

    def get_computers(
        self, ou_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the computers contained by this OU.

        Args:
            ou_id: The ID of the OU to query
            limit: Maximum number of computers to return
            skip: Number of computers to skip for pagination

        Returns:
            Dictionary with data (list of computers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/ous/{ou_id}/computers", params=params
        )

    def get_gpos(self, ou_id: str, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the GPOs that affect this OU.


        Args:
            ou_id: The ID of the OU to query
            limit: Maximum number of GPOs to return
            skip: Number of GPOs to skip for pagination

        Returns:
            Dictionary with data (list of GPOs) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/ous/{ou_id}/gpos", params=params
        )

    def get_groups(self, ou_id: str, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the groups contained by this OU.

        Args:
            ou_id: The ID of the OU to query
            limit: Maximum number of groups to return
            skip: Number of groups to skip for pagination

        Returns:
            Dictionary with data (list of groups) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/ous/{ou_id}/groups", params=params
        )

    def get_users(self, ou_id: str, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the users contained by this OU.

        Args:
            ou_id: The ID of the OU to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/ous/{ou_id}/users", params=params
        )