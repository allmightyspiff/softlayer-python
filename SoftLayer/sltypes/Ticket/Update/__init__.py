from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Ticket_Update(Entity):
    """The SoftLayer_Ticket_Update type relates to a single update to a ticket, either by a customer or an employee."""
    createDate: datetime
    editorId: int
    editorType: str
    entry: str
    id_: int
    ticketId: int
