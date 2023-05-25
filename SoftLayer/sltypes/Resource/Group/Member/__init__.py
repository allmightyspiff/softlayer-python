from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Resource_Group_Member(Entity):
    createDate: datetime
    id_: int
    status: str
