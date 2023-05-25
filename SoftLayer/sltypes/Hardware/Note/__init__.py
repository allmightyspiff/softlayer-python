from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Hardware_Note(Entity):
    createDate: datetime
    hardwareId: int
    id_: int
    modifyDate: datetime
    note: str
    typeId: int
    userRecordId: int
