from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Evault_WebCc_JobDetails(Entity):
    """The SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails will contain basic details for all backup and
restore jobs performed by the StorageLayer EVault service offering."""
    bytesUsed: int
    description: str
    hardwareId: int
    lastRunDate: datetime
    name: str
    originalSize: int
    percentageOfTotalUsage: int
    result: str
    virtualGuestId: int
