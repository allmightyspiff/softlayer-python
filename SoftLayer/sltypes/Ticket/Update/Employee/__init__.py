from SoftLayer.sltypes.Ticket.Update import Ticket_Update
from SoftLayer.sltypes.Ticket_Update import Ticket_Update
from SoftLayer import BaseClient

class Ticket_Update_Employee(Ticket_Update):
    """The SoftLayer_Ticket_Update_Employee data type models an update to a ticket made by a SoftLayer employee."""
    responseRating: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Update_Employee'

    def addResponseRating(self, identifier: int, responseRating: int, responseIndex: int) -> bool:
        """Set an update's response rating."""
        data = self.client.call('SoftLayer_Ticket_Update_Employee', 'addResponseRating', responseRating, responseIndex, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Ticket_Update_Employee':
        """Retrieve a SoftLayer_Ticket_Update_Employee record."""
        data = self.client.call('SoftLayer_Ticket_Update_Employee', 'getObject', id=identifier)
        from SoftLayer.sltypes.Ticket_Update_Employee import Ticket_Update_Employee
        return data
