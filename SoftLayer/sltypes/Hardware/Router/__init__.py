from SoftLayer.sltypes.Hardware.Switch import Hardware_Switch
from SoftLayer.sltypes.Hardware_Switch import Hardware_Switch
from SoftLayer import BaseClient

class Hardware_Router(Hardware_Switch):
    """The SoftLayer_Hardware_Router data type contains general information relating to a single SoftLayer router."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Router'

    def getObject(self, identifier: int) -> 'Hardware_Router':
        """Retrieve a SoftLayer_Hardware_Router record."""
        data = self.client.call('SoftLayer_Hardware_Router', 'getObject', id=identifier)
        return data

    def getBoundSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Router', 'getBoundSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getLocalDiskStorageCapabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Router', 'getLocalDiskStorageCapabilityFlag', id=identifier)
        return data

    def getSanStorageCapabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Router', 'getSanStorageCapabilityFlag', id=identifier)
        return data
