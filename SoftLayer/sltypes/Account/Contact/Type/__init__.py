from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Account_Contact_Type(Entity):
    createDate: datetime
    description: str
    id_: int
    keyName: str
    modifyDate: datetime
    name: str
