from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket_Survey(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Survey'

    def getPreference(self) -> None:
        data = self.client.call('SoftLayer_Ticket_Survey', 'getPreference')
        return data

    def optIn(self) -> None:
        data = self.client.call('SoftLayer_Ticket_Survey', 'optIn')
        return data

    def optOut(self) -> None:
        data = self.client.call('SoftLayer_Ticket_Survey', 'optOut')
        return data
