from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Gateway_Status(Entity):
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Gateway_Status'

    def getObject(self, identifier: int) -> 'Network_Gateway_Status':
        """Retrieve a SoftLayer_Network_Gateway_Status record."""
        data = self.client.call('SoftLayer_Network_Gateway_Status', 'getObject', id=identifier)
        return data
