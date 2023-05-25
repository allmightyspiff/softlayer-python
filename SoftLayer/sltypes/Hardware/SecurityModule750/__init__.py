from SoftLayer.sltypes.Hardware.SecurityModule import Hardware_SecurityModule
from SoftLayer.sltypes.Hardware_SecurityModule import Hardware_SecurityModule
from SoftLayer import BaseClient

class Hardware_SecurityModule750(Hardware_SecurityModule):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_SecurityModule750'

    def createObject(self, templateObject: 'Hardware_SecurityModule750') -> 'Hardware_SecurityModule750':
        """Create a new server"""
        data = self.client.call('SoftLayer_Hardware_SecurityModule750', 'createObject', templateObject)
        return data

    def getObject(self, identifier: int) -> 'Hardware_SecurityModule750':
        """Retrieve a SoftLayer_Hardware_SecurityModule750 record."""
        data = self.client.call('SoftLayer_Hardware_SecurityModule750', 'getObject', id=identifier)
        return data
