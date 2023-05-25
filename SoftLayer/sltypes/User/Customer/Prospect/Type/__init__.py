from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class User_Customer_Prospect_Type(Entity):
    createDate: datetime
    description: str
    id_: int
    keyName: str
    modifyDate: datetime
    name: str
