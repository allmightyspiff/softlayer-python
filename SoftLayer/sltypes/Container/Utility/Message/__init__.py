from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Utility_Message(Entity):
    createDate: datetime
    id_: int
    message: str
    modifyDate: datetime
    summary: str
