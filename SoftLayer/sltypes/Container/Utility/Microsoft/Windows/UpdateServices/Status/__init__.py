from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Utility_Microsoft_Windows_UpdateServices_Status(Entity):
    """SoftLayer customer servers that are purchased with the Microsoft Windows operating system are configured by
default to retrieve updates from SoftLayer's local Windows Server Update Services (WSUS) server.
Periodically, these servers synchronize and check for new updates from their local WSUS server.
SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status models the results of a server's last
synchronization attempt as queried from SoftLayer's WSUS servers."""
    lastRebootDate: datetime
    lastStatusDate: datetime
    lastSyncDate: datetime
    privateIPAddress: str
    syncStatus: str
    updateStatus: str
