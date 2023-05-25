from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Evault_WebCc_BackupResults(Entity):
    """The SoftLayer_Container_Network_Storage_Evault_WebCc_BackupResults will contain the timeframe of backups and
the results will also be returned."""
    beginTime: datetime
    conflict: str
    endTime: datetime
    failed: str
    success: str
