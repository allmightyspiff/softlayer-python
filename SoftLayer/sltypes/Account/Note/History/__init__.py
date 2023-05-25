from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Account_Note_History(Entity):
    accountNoteId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    note: str
    userId: int
