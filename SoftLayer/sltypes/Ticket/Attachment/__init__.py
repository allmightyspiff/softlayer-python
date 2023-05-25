from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Ticket_Attachment(Entity):
    """SoftLayer tickets have the ability to be associated with specific pieces of hardware in a customer's
inventory. Attaching hardware to a ticket can greatly increase response time from SoftLayer for issues that
are related to one or more specific servers on a customer's account. The SoftLayer_Ticket_Attachment_Hardware
data type models the relationship between a piece of hardware and a ticket. Only one attachment record may
exist per hardware item per ticket."""
    attachmentId: int
    createDate: datetime
    id_: int
    ticketId: int
