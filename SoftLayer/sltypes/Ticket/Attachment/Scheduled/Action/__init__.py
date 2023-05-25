from datetime import datetime
from SoftLayer.sltypes.Ticket.Attachment import Ticket_Attachment
from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment

class Ticket_Attachment_Scheduled_Action(Ticket_Attachment):
    runDate: datetime
    transactionId: int
