from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Schedule_Property(Entity):
    """Schedule properties provide attributes such as start date, end date, interval, and other properties to a
storage schedule."""
    createDate: datetime
    id_: int
    modifyDate: datetime
    typeId: int
    value: str
