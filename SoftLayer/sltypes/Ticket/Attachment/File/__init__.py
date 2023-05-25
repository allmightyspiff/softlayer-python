from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket_Attachment_File(Entity):
    """SoftLayer tickets can have have files attached to them. Attaching a file to a ticket is a good way to report
issues, provide documentation, and give examples of an issue. Both SoftLayer customers and employees have the
ability to attach files to a ticket. The SoftLayer_Ticket_Attachment_File data type models a single file
attached to a ticket."""
    createDate: datetime
    fileName: str
    fileSize: str
    id_: int
    modifyDate: datetime
    ticketId: int
    updateId: int
    uploaderId: str
    uploaderType: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Attachment_File'

    def getExtensionWhitelist(self) -> list[str]:
        data = self.client.call('SoftLayer_Ticket_Attachment_File', 'getExtensionWhitelist')
        return data

    def getObject(self, identifier: int) -> 'Ticket_Attachment_File':
        """Retrieve a SoftLayer_Ticket_Attachment_File record."""
        data = self.client.call('SoftLayer_Ticket_Attachment_File', 'getObject', id=identifier)
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Ticket_Attachment_File', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getUpdate(self, identifier: int) -> 'Ticket_Update':
        """"""
        data = self.client.call('SoftLayer_Ticket_Attachment_File', 'getUpdate', id=identifier)
        from SoftLayer.sltypes.Ticket_Update import Ticket_Update
        return data
