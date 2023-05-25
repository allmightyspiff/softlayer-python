from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Resource_Group_Attribute(Entity):
    createDate: datetime
    id_: int
    value: str
