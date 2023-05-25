from SoftLayer.sltypes.User.Customer.External.Binding import User_Customer_External_Binding
from SoftLayer.sltypes.User_Customer_External_Binding import User_Customer_External_Binding
from SoftLayer import BaseClient

class User_Customer_External_Binding_Totp(User_Customer_External_Binding):
    """The SoftLayer_User_Customer_External_Binding_Totp data type contains information about a single time-based
one time password external binding.  The external binding information is used when a SoftLayer customer logs
into the SoftLayer customer portal to authenticate them.   The information provided by this external binding
data type includes:  * The type of credential * The current state of the credential ** Active ** Inactive
SoftLayer users with an active external binding will be prohibited from using the API for security reasons."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_External_Binding_Totp'

    def activate(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Totp', 'activate', id=identifier)
        return data

    def deactivate(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Totp', 'deactivate', id=identifier)
        return data

    def generateSecretKey(self) -> str:
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Totp', 'generateSecretKey')
        return data

    def getObject(self, identifier: int) -> 'User_Customer_External_Binding_Totp':
        """Retrieve a SoftLayer_User_Customer_External_Binding_Totp record."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Totp', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_External_Binding_Totp import User_Customer_External_Binding_Totp
        return data
