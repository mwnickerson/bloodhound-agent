from typing import Any, Dict, Optional

from .base import BloodhoundBaseClient


class GraphClient:
    """Client for Graph related Bloodhound API Endpoints"""

    def __init__(self, base_client: BloodhoundBaseClient):
        self.base_client = base_client

    # I am getting a 401 error when searching for some objects and it works on others
    # for example if i search for Domain Admins it fails with a 401 error but if i search for TargetUserB it works fine
    def search(self, query: str, search_type: str = "fuzzy") -> Dict[str, Any]:
        """
        Search for nodes in the graph by name

        Args:
            query: Search query text
            search_type: Type of search strategy ('fuzzy' or 'exact')

        Returns:
            Search results
        """
        params = {"query": query, "type": search_type}
        return self.base_client.request("GET", "/api/v2/graph-search", params=params)

    def get_shortest_path(
        self, start_node: str, end_node: str, relationship_kinds: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get the shortest path between two nodes in the graph

        Args:
            start_node: The object ID of the starting node
            end_node: The object ID of the ending node
            relationship_kinds: Optional filter for relationship types

        Returns:
            Graph data of the shortest path
        """
        params = {"start_node": start_node, "end_node": end_node}

        if relationship_kinds:
            params["relationshipkinds"] = relationship_kinds

        return self.base_client.request(
            "GET", "/api/v2/graphs/shortest-path", params=params
        )

    def get_edge_composition(
        self, source_node: int, target_node: int, edge_type: str
    ) -> Dict[str, Any]:
        """
        Get the composition of a complex edge between two nodes

        Args:
            source_node: ID of the source node
            target_node: ID of the target node
            edge_type: Type of edge to analyze

        Returns:
            Graph data showing the composition of the edge
        """
        params = {
            "sourcenode": source_node,
            "targetnode": target_node,
            "edgetype": edge_type,
        }

        return self.base_client.request(
            "GET", "/api/v2/graphs/edge-composition", params=params
        )

    def get_relay_targets(
        self, source_node: int, target_node: int, edge_type: str
    ) -> Dict[str, Any]:
        """
        Get nodes that are valid relay targets for a given edge

        Args:
            source_node: ID of the source node
            target_node: ID of the target node
            edge_type: Type of edge

        Returns:
            Graph data with valid relay targets
        """
        params = {
            "sourcenode": source_node,
            "targetnode": target_node,
            "edgetype": edge_type,
        }

        return self.base_client.request(
            "GET", "/api/v2/graphs/relay-targets", params=params
        )