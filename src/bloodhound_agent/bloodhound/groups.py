from typing import Any, Dict

from .base import BloodhoundBaseClient


class GroupClient:
    """Client for group-related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_info(self, group_id: str) -> Dict[str, Any]:
        """
        Get information about a specific group

        Args:
            group_id: The ID of the group to query

        Returns:
            Group information dictionary
        """
        params = {"counts": "true"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}", params=params
        )

    def get_admin_rights(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get administrative rights of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of rights to return
            skip: Number of rights to skip for pagination

        Returns:
            Dictionary with data (list of rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/admin-rights", params=params
        )

    def get_controllables(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllable objects for a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of controllables to return
            skip: Number of controllables to skip for pagination

        Returns:
            Dictionary with data (list of controllables) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/controllables", params=params
        )

    def get_controllers(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/controllers", params=params
        )

    def get_dcom_rights(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get DCOM rights of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of DCOM rights to return
            skip: Number of DCOM rights to skip for pagination

        Returns:
            Dictionary with data (list of DCOM rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/dcom-rights", params=params
        )

    def get_members(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get members of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of members to return
            skip: Number of members to skip for pagination

        Returns:
            Dictionary with data (list of members) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/members", params=params
        )

    def get_memberships(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get group memberships of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of memberships to return
            skip: Number of memberships to skip for pagination

        Returns:
            Dictionary with data (list of memberships) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/memberships", params=params
        )

    def get_ps_remote_rights(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get PowerShell Remote rights of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of PS Remote rights to return
            skip: Number of PS Remote rights to skip for pagination

        Returns:
            Dictionary with data (list of PS Remote rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/ps-remote-rights", params=params
        )

    def get_rdp_rights(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get RDP rights of a specific group
        Args:
            group_id: The ID of the group to query
            limit: Maximum number of RDP rights to return
            skip: Number of RDP rights to skip for pagination
        Returns:
            Dictionary with data (list of RDP rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/rdp-rights", params=params
        )

    def get_sessions(
        self, group_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get active sessions of a specific group

        Args:
            group_id: The ID of the group to query
            limit: Maximum number of sessions to return
            skip: Number of sessions to skip for pagination

        Returns:
            Dictionary with data (list of sessions) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/groups/{group_id}/sessions", params=params
        )