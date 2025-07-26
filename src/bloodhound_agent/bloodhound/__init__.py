"""
BloodHound API Client Package
This package provides a client for interacting with the BloodHound API.
"""
from .base import (
    BloodhoundBaseClient,
    BloodhoundError,
    BloodhoundAuthError,
    BloodhoundConnectionError,
    BloodhoundAPIError,
)
from .domains import DomainClient
from .users import UserClient
from .groups import GroupClient
from .computers import ComputerClient
from .ous import OUsClient
from .gpos import GPOsClient
from .graph import GraphClient
from .adcs import ADCSClient
from .cypher import CypherClient

from .api import BloodhoundAPI

# package version
__version__ = "1.0.0"

# define what gets imported with 'from bloodhound import *'
__all__ = [
    # main api class
    "BloodhoundAPI",
    # base client and errors
    "BloodhoundBaseClient",
    "BloodhoundError",
    "BloodhoundAuthError",
    "BloodhoundConnectionError",
    "BloodhoundAPIError",
    # individual clients
    "DomainClient",
    "UserClient",
    "GroupClient",
    "ComputerClient",
    "OUsClient",
    "GPOsClient",
    "GraphClient",
    "ADCSClient",
    "CypherClient",
]


