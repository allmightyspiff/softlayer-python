from SoftLayer.sltypes.User.External.Binding.Vendor import User_External_Binding_Vendor
from SoftLayer.sltypes.User_External_Binding_Vendor import User_External_Binding_Vendor
from SoftLayer import BaseClient

class User_Customer_External_Binding_Vendor(User_External_Binding_Vendor):
    """The SoftLayer_User_Customer_External_Binding_Vendor data type contains information for a single external
binding vendor.  This information includes a user friendly vendor name, a unique version of the vendor name,
and a unique internal identifier that can be used when creating a new external binding."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_External_Binding_Vendor'

    def getObject(self, identifier: int) -> 'User_Customer_External_Binding_Vendor':
        """Retrieve a SoftLayer_User_Customer_External_Binding_Vendor record."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Vendor', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_External_Binding_Vendor import User_Customer_External_Binding_Vendor
        return data
