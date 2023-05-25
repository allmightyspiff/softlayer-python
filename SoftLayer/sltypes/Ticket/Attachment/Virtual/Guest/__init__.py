from SoftLayer.sltypes.Ticket.Attachment import Ticket_Attachment
from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment

class Ticket_Attachment_Virtual_Guest(Ticket_Attachment):
    """SoftLayer tickets have the ability to be associated with specific virtual guests in a customer's inventory.
Attaching virtual guests to a ticket can greatly increase response time from SoftLayer for issues that are
related to one or more specific servers on a customer's account. The
SoftLayer_Ticket_Attachment_Virtual_Guest data type models the relationship between a virtual guest and a
ticket. Only one attachment record may exist per virtual guest per ticket."""
    virtualGuestId: int
