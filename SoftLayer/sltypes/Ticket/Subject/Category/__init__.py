from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket_Subject_Category(Entity):
    """SoftLayer_Ticket_Subject_Category groups ticket subjects into logical group."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Subject_Category'

    def getAllObjects(self) -> list['Ticket_Subject_Category']:
        """Retrieve all ticket subject categories."""
        data = self.client.call('SoftLayer_Ticket_Subject_Category', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Ticket_Subject_Category':
        """Retrieve a SoftLayer_Ticket_Subject_Category record."""
        data = self.client.call('SoftLayer_Ticket_Subject_Category', 'getObject', id=identifier)
        return data

    def getSubjects(self, identifier: int) -> list['Ticket_Subject']:
        """"""
        data = self.client.call('SoftLayer_Ticket_Subject_Category', 'getSubjects', id=identifier)
        from SoftLayer.sltypes.Ticket_Subject import Ticket_Subject
        return data
