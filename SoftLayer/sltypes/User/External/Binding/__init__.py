from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_External_Binding(Entity):
    """The SoftLayer_User_External_Binding data type contains general information for a single external binding.
This includes the 3rd party vendor, type of binding, and a unique identifier and password that is used to
authenticate against the 3rd party service."""
    active: bool
    createDate: datetime
    externalId: str
    id_: int
    password: str
    typeId: int
    userId: int
    vendorId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_External_Binding'

    def deleteObject(self, identifier: int) -> bool:
        """Delete an external authentication binding."""
        data = self.client.call('SoftLayer_User_External_Binding', 'deleteObject', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'User_External_Binding':
        """Retrieve a SoftLayer_User_External_Binding record."""
        data = self.client.call('SoftLayer_User_External_Binding', 'getObject', id=identifier)
        return data

    def updateNote(self, identifier: int, text: str) -> bool:
        """Update the note of an external binding."""
        data = self.client.call('SoftLayer_User_External_Binding', 'updateNote', text, id=identifier)
        return data

    def getAttributes(self, identifier: int) -> list['User_External_Binding_Attribute']:
        """"""
        data = self.client.call('SoftLayer_User_External_Binding', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.User_External_Binding_Attribute import User_External_Binding_Attribute
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_User_External_Binding', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getNote(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_User_External_Binding', 'getNote', id=identifier)
        return data

    def getType(self, identifier: int) -> 'User_External_Binding_Type':
        """"""
        data = self.client.call('SoftLayer_User_External_Binding', 'getType', id=identifier)
        from SoftLayer.sltypes.User_External_Binding_Type import User_External_Binding_Type
        return data

    def getVendor(self, identifier: int) -> 'User_External_Binding_Vendor':
        """"""
        data = self.client.call('SoftLayer_User_External_Binding', 'getVendor', id=identifier)
        from SoftLayer.sltypes.User_External_Binding_Vendor import User_External_Binding_Vendor
        return data
