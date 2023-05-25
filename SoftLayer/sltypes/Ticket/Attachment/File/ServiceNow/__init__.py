from SoftLayer.sltypes.Ticket.Attachment.File import Ticket_Attachment_File
from SoftLayer.sltypes.Ticket_Attachment_File import Ticket_Attachment_File
from SoftLayer import BaseClient

class Ticket_Attachment_File_ServiceNow(Ticket_Attachment_File):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Attachment_File_ServiceNow'

    def getObject(self, identifier: int) -> 'Ticket_Attachment_File_ServiceNow':
        """Retrieve a SoftLayer_Ticket_Attachment_File_ServiceNow record."""
        data = self.client.call('SoftLayer_Ticket_Attachment_File_ServiceNow', 'getObject', id=identifier)
        return data
