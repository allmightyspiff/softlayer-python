from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Event(Entity):
    """Storage volumes can create various events to keep track of what has occurred to the volume. Events provide an
audit trail that can be used to verify that various tasks have occurred, such as snapshots to be created by a
schedule or remote replication synchronization."""
    createDate: datetime
    message: str
    scheduleId: int
    typeId: int
    volumeId: int
