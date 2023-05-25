from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network'

    def connectPrivateEndpointService(self) -> bool:
        """Establishes a connection between the account and Service Endpoint networks."""
        data = self.client.call('SoftLayer_Network', 'connectPrivateEndpointService')
        return data

    def disconnectPrivateEndpointService(self) -> bool:
        """Terminates the connection between the account and Service Endpoint networks."""
        data = self.client.call('SoftLayer_Network', 'disconnectPrivateEndpointService')
        return data

    def getObject(self, identifier: int) -> 'Network':
        """Retrieve a SoftLayer_Network record."""
        data = self.client.call('SoftLayer_Network', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network import Network
        return data

    def isConnectedToPrivateEndpointService(self) -> bool:
        """Checks the current Service Endpoint network connection status."""
        data = self.client.call('SoftLayer_Network', 'isConnectedToPrivateEndpointService')
        return data
