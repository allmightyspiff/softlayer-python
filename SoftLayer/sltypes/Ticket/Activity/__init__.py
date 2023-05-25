from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Ticket_Activity(Entity):
    createDate: datetime
    createTimestamp: datetime
    id_: int
    value: str
