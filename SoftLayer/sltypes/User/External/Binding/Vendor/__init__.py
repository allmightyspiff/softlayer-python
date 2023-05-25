from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_External_Binding_Vendor(Entity):
    """The SoftLayer_User_External_Binding_Vendor data type contains information for a single external binding
vendor.  This information includes a user friendly vendor name, a unique version of the vendor name, and a
unique internal identifier that can be used when creating a new external binding."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_External_Binding_Vendor'

    def getAllObjects(self) -> list['User_External_Binding_Vendor']:
        """Get a list of all available external binding vendors that SoftLayer supports."""
        data = self.client.call('SoftLayer_User_External_Binding_Vendor', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'User_External_Binding_Vendor':
        """Retrieve a SoftLayer_User_External_Binding_Vendor record."""
        data = self.client.call('SoftLayer_User_External_Binding_Vendor', 'getObject', id=identifier)
        return data
