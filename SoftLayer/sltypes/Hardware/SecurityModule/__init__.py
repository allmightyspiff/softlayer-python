from SoftLayer.sltypes.Hardware.Server import Hardware_Server
from SoftLayer.sltypes.Hardware_Server import Hardware_Server
from SoftLayer import BaseClient

class Hardware_SecurityModule(Hardware_Server):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_SecurityModule'

    def createObject(self, templateObject: 'Hardware_SecurityModule') -> 'Hardware_SecurityModule':
        """Create a new server"""
        data = self.client.call('SoftLayer_Hardware_SecurityModule', 'createObject', templateObject)
        return data

    def getObject(self, identifier: int) -> 'Hardware_SecurityModule':
        """Retrieve a SoftLayer_Hardware_SecurityModule record."""
        data = self.client.call('SoftLayer_Hardware_SecurityModule', 'getObject', id=identifier)
        return data
