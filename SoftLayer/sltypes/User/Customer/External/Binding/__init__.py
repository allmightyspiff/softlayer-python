from SoftLayer.sltypes.User.External.Binding import User_External_Binding
from SoftLayer.sltypes.User_External_Binding import User_External_Binding
from SoftLayer import BaseClient

class User_Customer_External_Binding(User_External_Binding):
    """The SoftLayer_User_Customer_External_Binding data type contains general information for a single external
binding.  This includes the 3rd party vendor, type of binding, and a unique identifier and password that is
used to authenticate against the 3rd party service."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_External_Binding'

    def disable(self, identifier: int, reason: str) -> bool:
        """Disable an external binding."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding', 'disable', reason, id=identifier)
        return data

    def enable(self, identifier: int) -> bool:
        """Enable an external binding."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding', 'enable', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_External_Binding':
        """Retrieve a SoftLayer_User_Customer_External_Binding record."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding', 'getObject', id=identifier)
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_External_Binding', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
