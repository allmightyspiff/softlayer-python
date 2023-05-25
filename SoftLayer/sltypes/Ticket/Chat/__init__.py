from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Ticket_Chat(Entity):
    customerId: int
    endDate: datetime
    startDate: datetime
    transcript: str
