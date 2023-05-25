from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket_Priority(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Priority'

    def getPriorities(self) -> list['Container_Ticket_Priority']:
        """Obtain a container of valid ticket priority values with value/name key pairs."""
        data = self.client.call('SoftLayer_Ticket_Priority', 'getPriorities')
        from SoftLayer.sltypes.Container_Ticket_Priority import Container_Ticket_Priority
        return data
