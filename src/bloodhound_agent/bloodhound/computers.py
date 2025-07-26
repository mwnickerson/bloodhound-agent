from typing import Any, Dict

from .base import BloodhoundBaseClient


class ComputerClient:
    """Client for computer-related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_info(self, computer_id: str) -> Dict[str, Any]:
        """
        Get information about a specific computer

        Args:
            computer_id: The ID of the computer to query

        Returns:
            Computer information dictionary
        """
        params = {"counts": "true"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}", params=params
        )

    def get_admin_rights(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get administrative rights of a specific computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of rights to return
            skip: Number of rights to skip for pagination

        Returns:
            Dictionary with data (list of rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/admin-rights", params=params
        )

    def get_admin_users(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get administrative users of a specific computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/admin-users", params=params
        )

    def get_constrained_delegation_rights(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the principals that this computer has constrained delegations rights to.
        This is a list of the computers that this computer can impersonate.

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of rights to return
            skip: Number of rights to skip for pagination

        Returns:
            Dictionary with data (list of rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET",
            f"/api/v2/computers/{computer_id}/constrained-delegation-rights",
            params=params,
        )

    def get_constrained_users(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the principals that have constrained delegation rights to this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/constrained-users", params=params
        )

    def get_controllables(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the principals this computer can control.


        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of controllables to return
            skip: Number of controllables to skip for pagination

        Returns:
            Dictionary with data (list of controllables) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/controllables", params=params
        )

    def get_controllers(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the principals that can control this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/controllers", params=params
        )

    def get_dcom_rights(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the systems this computer can execute DCOM on.
        This is a list of the computers that this computer can impersonate.

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of DCOM rights to return
            skip: Number of DCOM rights to skip for pagination

        Returns:
            Dictionary with data (list of DCOM rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/dcom-rights", params=params
        )

    def get_dcom_users(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the users that have DCOM rights to this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/dcom-users", params=params
        )

    def get_group_membership(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the groups this computer is a member of

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of memberships to return
            skip: Number of memberships to skip for pagination

        Returns:
            Dictionary with data (list of memberships) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/group-membership", params=params
        )

    def get_ps_remote_rights(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the systems this computer has remote PowerShell rights on.


        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of PS Remote rights to return
            skip: Number of PS Remote rights to skip for pagination

        Returns:
            Dictionary with data (list of PS Remote rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/ps-remote-rights", params=params
        )

    def get_ps_remote_users(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the users that have remote PowerShell rights to this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/ps-remote-users", params=params
        )

    def get_rdp_rights(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the systems this computer has RDP rights on.

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of RDP rights to return
            skip: Number of RDP rights to skip for pagination
        Returns:
            Dictionary with data (list of RDP rights) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/rdp-rights", params=params
        )

    def get_rdp_users(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the users that have RDP rights to this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/rdp-users", params=params
        )

    def get_sessions(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the principals with active sessions on this computer.

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of sessions to return
            skip: Number of sessions to skip for pagination

        Returns:
            Dictionary with data (list of sessions) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/sessions", params=params
        )

    def get_sql_admins(
        self, computer_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get a list, graph, or count of the SQL administrators on this computer

        Args:
            computer_id: The ID of the computer to query
            limit: Maximum number of SQL admins to return
            skip: Number of SQL admins to skip for pagination

        Returns:
            Dictionary with data (list of SQL admins) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/computers/{computer_id}/sql-admins", params=params
        )