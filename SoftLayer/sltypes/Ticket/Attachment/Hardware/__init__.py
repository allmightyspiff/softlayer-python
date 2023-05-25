from SoftLayer.sltypes.Ticket.Attachment import Ticket_Attachment
from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment

class Ticket_Attachment_Hardware(Ticket_Attachment):
    """SoftLayer tickets have the ability to be associated with specific pieces of hardware in a customer's
inventory. Attaching hardware to a ticket can greatly increase response time from SoftLayer for issues that
are related to one or more specific servers on a customer's account. The SoftLayer_Ticket_Attachment_Hardware
data type models the relationship between a piece of hardware and a ticket. Only one attachment record may
exist per hardware item per ticket."""
    hardwareId: int
