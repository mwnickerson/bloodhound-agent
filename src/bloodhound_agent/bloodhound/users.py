from typing import Any, Dict

from .base import BloodhoundBaseClient


class UserClient:
    """Client for user-related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_info(self, user_id: str) -> Dict[str, Any]:
        """
        Get information about a specific user

        Args:
            user_id: The ID of the user to query

        Returns:
            User information dictionary
        """
        params = {"counts": "true"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}", params=params
        )

    def get_admin_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get administrative rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of rights to return
            skip: Number of rights to skip for pagination

        Returns:
            Dictionary with data (list of rights) and count (total number of rights)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/admin-rights", params=params
        )

    def get_constrained_delegation_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get constrained delegation rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of constrained delegation rights to return
            skip: Number of constrained delegation rights to skip for pagination

        Returns:
            Dictionary with data (list of rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET",
            f"/api/v2/users/{user_id}/constrained-delegation-rights",
            params=params,
        )

    def get_controllables(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllable objects for a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of controllables to return
            skip: Number of controllables to skip for pagination

        Returns:
            Dictionary with data (list of controllables) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/controllables", params=params
        )

    def get_controllers(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/controllers", params=params
        )

    def get_dcom_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get DCOM rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of DCOM rights to return
            skip: Number of DCOM rights to skip for pagination

        Returns:
            Dictionary with data (list of DCOM rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/dcom-rights", params=params
        )

    def get_memberships(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get group memberships of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of memberships to return
            skip: Number of memberships to skip for pagination

        Returns:
            Dictionary with data (list of memberships) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/memberships", params=params
        )

    def get_ps_remote_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get PowerShell Remote rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of PS Remote rights to return
            skip: Number of PS Remote rights to skip for pagination

        Returns:
            Dictionary with data (list of PS Remote rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/ps-remote-rights", params=params
        )

    def get_rdp_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get RDP rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of RDP rights to return
            skip: Number of RDP rights to skip for pagination

        Returns:
            Dictionary with data (list of RDP rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/rdp-rights", params=params
        )

    def get_sessions(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get active sessions of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of sessions to return
            skip: Number of sessions to skip for pagination

        Returns:
            Dictionary with data (list of sessions) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/sessions", params=params
        )

    def get_sql_admin_rights(
        self, user_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get SQL admin rights of a specific user

        Args:
            user_id: The ID of the user to query
            limit: Maximum number of SQL admin rights to return
            skip: Number of SQL admin rights to skip for pagination

        Returns:
            Dictionary with data (list of SQL admin rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/users/{user_id}/sql-admin-rights", params=params
        )