from typing import Any, Dict, List

from .base import BloodhoundBaseClient


class DomainClient:
    """Client for domain-related BloodHound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Get all domains in the Bloodhound CE Instance

        Returns:
            List of domain information dictionaries
        """
        response = self.base_client.request("GET", "/api/v2/available-domains")
        return response["data"]

    def search_objects(
        self, query: str, type: str = None, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Search for objects by name, Object ID. They can also be filtered by type.
        Args:
            query: search parameter for the name or object ID of the node (required)
            type: type of object to search for (optional)
                - For AD: Base, User, Computer, Group, Container, GPO, OU, Cert template, Trust
                - For Azure: AZBase, AZbase, AZDevice
            skip: Number of results to skip for pagination (default: 0) (optional)
            limit: Maximum number of results to return (default: 100) (optional)

            Returns:
                Dictionary with information on the object found. The information includes:
                - objectid: Object ID
                - type: the type of the object
                - name: Name of the object
                - distinguishedname : Distinguished Name of the object
                - system_tags: System tags associated with the object
        """
        params = {
            "q": query,  # Changed from "query" to "q" to match the API
            "limit": limit,
            "skip": skip,
        }

        # Only add the type parameter if it's provided
        if type:
            params["type"] = type

        return self.base_client.request("GET", "/api/v2/search", params=params)

    def get_users(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get users in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of users to return
            skip: Number of users to skip for pagination

        Returns:
            Dictionary with data (list of users) and count (total number of users)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/users", params=params
        )

    def get_groups(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get groups in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of groups to return
            skip: Number of groups to skip for pagination

        Returns:
            Dictionary with data (list of groups) and count (total number of groups)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/groups", params=params
        )

    def get_computers(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get computers in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of computers to return
            skip: Number of computers to skip for pagination

        Returns:
            Dictionary with data (list of computers) and count (total number of computers)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/computers", params=params
        )

    def get_controllers(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/controllers", params=params
        )

    def get_gpos(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get Group Policy Objects (GPOs) in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of GPOs to return
            skip: Number of GPOs to skip for pagination

        Returns:
            Dictionary with data (list of GPOs) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/gpos", params=params
        )

    def get_ous(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get Organizational Units (OUs) in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of OUs to return
            skip: Number of OUs to skip for pagination

        Returns:
            Dictionary with data (list of OUs) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/ous", params=params
        )

    def get_dc_syncers(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get DC Syncers in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of DC Syncers to return
            skip: Number of DC Syncers to skip for pagination

        Returns:
            Dictionary with data (list of DC Syncers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/dc-syncers", params=params
        )

    def get_foreign_admins(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get foreign admins in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of foreign admins to return
            skip: Number of foreign admins to skip for pagination

        Returns:
            Dictionary with data (list of foreign admins) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/foreign-admins", params=params
        )

    def get_foreign_gpo_controllers(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get foreign GPO controllers in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of foreign GPO controllers to return
            skip: Number of foreign GPO controllers to skip for pagination

        Returns:
            Dictionary with data (list of foreign GPO controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/foreign-gpo-controllers", params=params
        )

    def get_foreign_groups(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get foreign groups in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of foreign groups to return
            skip: Number of foreign groups to skip for pagination

        Returns:
            Dictionary with data (list of foreign groups) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/foreign-groups", params=params
        )

    def get_foreign_users(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get foreign users in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of foreign users to return
            skip: Number of foreign users to skip for pagination

        Returns:
            Dictionary with data (list of foreign users) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/foreign-users", params=params
        )

    def get_inbound_trusts(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get inbound trusts in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of inbound trusts to return
            skip: Number of inbound trusts to skip for pagination

        Returns:
            Dictionary with data (list of inbound trusts) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/inbound-trusts", params=params
        )

    def get_outbound_trusts(
        self, domain_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get outbound trusts in a specific domain

        Args:
            domain_id: The ID of the domain to query
            limit: Maximum number of outbound trusts to return
            skip: Number of outbound trusts to skip for pagination

        Returns:
            Dictionary with data (list of outbound trusts) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/domains/{domain_id}/outbound-trusts", params=params
        )