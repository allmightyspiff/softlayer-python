from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_SSLCipher(Entity):
    """The SoftLayer_Network_LBaaS_SSLCipher type presents a structure that contains attributes of load balancer
cipher suites."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_SSLCipher'

    def getAllObjects(self) -> list['Network_LBaaS_SSLCipher']:
        """Get all supported ciphers."""
        data = self.client.call('SoftLayer_Network_LBaaS_SSLCipher', 'getAllObjects')
        from SoftLayer.sltypes.Network_LBaaS_SSLCipher import Network_LBaaS_SSLCipher
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_SSLCipher':
        """Retrieve a SoftLayer_Network_LBaaS_SSLCipher record."""
        data = self.client.call('SoftLayer_Network_LBaaS_SSLCipher', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_SSLCipher import Network_LBaaS_SSLCipher
        return data
