from SoftLayer.sltypes.Ticket.Attachment import Ticket_Attachment
from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment

class Ticket_Attachment_Dedicated_Host(Ticket_Attachment):
    """SoftLayer tickets have the ability to be associated with specific dedicated hosts in a customer's inventory.
Attaching a dedicated host to a ticket can greatly increase response time from SoftLayer for issues that are
related to one or more specific hosts on a customer's account. The SoftLayer_Ticket_Attachment_Dedicated_Host
data type models the relationship between a dedicated host and a ticket. Only one attachment record can exist
per dedicated host item per ticket."""
    dedicatedHostId: int
