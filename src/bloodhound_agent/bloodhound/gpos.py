from typing import Any, Dict

from .base import BloodhoundBaseClient


class GPOsClient:
    """Client for GPO related Bloodhound API Endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_info(self, gpo_id: str) -> Dict[str, Any]:
        """
        Get information about a specific GPO

        Args:
            gpo_id: The ID of the GPO to query

        Returns:
            GPO information dictionary
        """
        params = {"counts": "true"}
        return self.base_client.request("GET", f"/api/v2/gpos/{gpo_id}", params=params)

    def get_computer(
        self, gpo_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the computers that this GPO applies to.

        Args:
            gpo_id: The ID of the GPO to query
            limit: Maximum number of computers to return
            skip: Number of computers to skip for pagination

        Returns:
            Dictionary with data (list of computers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/gpos/{gpo_id}/computers", params=params
        )

    def get_controllers(
        self, gpo_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the Security Principals that can control this GPO.

        Args:
            gpo_id: The ID of the GPO to query
            limit: the maximum number of controller security principals to return (default is 100)
            skip: Number of controller security principals to skip for pagination (Default is 0)

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/gpos/{gpo_id}/controllers", params=params
        )

    def get_ous(self, gpo_id: str, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the OUs that this GPO applies to.

        Args:
            gpo_id: The ID of the GPO to query
            limit: Maximum number of OUs to return
            skip: Number of OUs to skip for pagination

        Returns:
            Dictionary with data (list of OUs) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/gpos/{gpo_id}/ous", params=params
        )

    def get_tier_zeros(
        self, gpo_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the Tier zero security principals that this GPO applies to.

        Args:
            gpo_id: The ID of the GPO to query
            limit: Maximum number of Tier 0s to return
            skip: Number of Tier 0s to skip for pagination

        Returns:
            Dictionary with data (list of Tier 0s) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/gpos/{gpo_id}/tier-zeros", params=params
        )

    def get_users(self, gpo_id: str, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the users that this GPO applies to.

        Args:
            gpo_id: The ID of the GPO to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/gpos/{gpo_id}/users", params=params
        )