from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_DirectLink_Provider(Entity):
    """The SoftLayer_Network_DirectLink_Provider presents a structure containing attributes of a Direct Link
provider."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_DirectLink_Provider'

    def getObject(self, identifier: int) -> 'Network_DirectLink_Provider':
        """Retrieve a SoftLayer_Network_DirectLink_Provider record."""
        data = self.client.call('SoftLayer_Network_DirectLink_Provider', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_DirectLink_Provider import Network_DirectLink_Provider
        return data
