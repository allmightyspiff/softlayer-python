from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Property(Entity):
    """A property provides additional information about a volume which it is assigned to. This information can range
from "Mountable" flags to utilized snapshot space."""
    createDate: datetime
    modifyDate: datetime
    value: str
    volumeId: int
