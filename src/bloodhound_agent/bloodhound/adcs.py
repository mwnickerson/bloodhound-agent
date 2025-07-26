from typing import Any, Dict

from .base import BloodhoundBaseClient


class ADCSClient:
    """Client for ADCS-related Bloodhound API endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    # Certificate Templates methods
    def get_cert_template_info(self, template_id: str) -> Dict[str, Any]:
        """
        Get information about a specific Certificate Template

        Args:
            template_id: The ID of the Certificate Template to query

        Returns:
            Certificate Template information dictionary
        """
        return self.base_client.request("GET", f"/api/v2/certtemplates/{template_id}")

    def get_cert_template_controllers(
        self, template_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific Certificate Template

        Args:
            template_id: The ID of the Certificate Template to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/certtemplates/{template_id}/controllers", params=params
        )

    # Root Certificate Authorities methods
    def get_root_ca_info(self, ca_id: str) -> Dict[str, Any]:
        """
        Get information about a specific Root Certificate Authority

        Args:
            ca_id: The ID of the Root CA to query

        Returns:
            Root CA information dictionary
        """
        return self.base_client.request("GET", f"/api/v2/rootcas/{ca_id}")

    def get_root_ca_controllers(
        self, ca_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific Root Certificate Authority

        Args:
            ca_id: The ID of the Root CA to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/rootcas/{ca_id}/controllers", params=params
        )

    # Enterprise Certificate Authorities methods
    def get_enterprise_ca_info(self, ca_id: str) -> Dict[str, Any]:
        """
        Get information about a specific Enterprise Certificate Authority

        Args:
            ca_id: The ID of the Enterprise CA to query

        Returns:
            Enterprise CA information dictionary
        """
        return self.base_client.request("GET", f"/api/v2/enterprisecas/{ca_id}")

    def get_enterprise_ca_controllers(
        self, ca_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific Enterprise Certificate Authority

        Args:
            ca_id: The ID of the Enterprise CA to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/enterprisecas/{ca_id}/controllers", params=params
        )

    # AIA Certificate Authorities methods
    def get_aia_ca_controllers(
        self, ca_id: str, limit: int = 100, skip: int = 0
    ) -> Dict[str, Any]:
        """
        Get controllers of a specific AIA Certificate Authority

        Args:
            ca_id: The ID of the AIA CA to query
            limit: Maximum number of controllers to return
            skip: Number of controllers to skip for pagination

        Returns:
            Dictionary with data (list of controllers) and count (total number)
        """
        params = {"limit": limit, "skip": skip, "type": "list"}
        return self.base_client.request(
            "GET", f"/api/v2/aia-cas/{ca_id}/controllers", params=params
        )