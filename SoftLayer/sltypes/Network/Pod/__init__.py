from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Pod(Entity):
    backendRouterId: int
    backendRouterName: str
    capabilities: list[str]
    datacenterId: int
    datacenterLongName: str
    datacenterName: str
    frontendRouterId: int
    frontendRouterName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Pod'

    def getAllObjects(self) -> list['Network_Pod']:
        """Retrieve a list of Pods; optionally filtered via datacenter and/or capabilities."""
        data = self.client.call('SoftLayer_Network_Pod', 'getAllObjects')
        from SoftLayer.sltypes.Network_Pod import Network_Pod
        return data

    def getCapabilities(self, identifier: int) -> list[str]:
        """Retrieve capabilities for the Pod."""
        data = self.client.call('SoftLayer_Network_Pod', 'getCapabilities', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Pod':
        """Retrieve a Pod by name."""
        data = self.client.call('SoftLayer_Network_Pod', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Pod import Network_Pod
        return data

    def listCapabilities(self) -> list[str]:
        """Retrieve a list of all possible capabilities Pods may fulfill."""
        data = self.client.call('SoftLayer_Network_Pod', 'listCapabilities')
        return data
