from SoftLayer.sltypes.User.Customer.External.Binding import User_Customer_External_Binding
from SoftLayer.sltypes.User_Customer_External_Binding import User_Customer_External_Binding
from SoftLayer import BaseClient

class User_Customer_External_Binding_Verisign(User_Customer_External_Binding):
    """The SoftLayer_User_Customer_External_Binding_Verisign data type contains information about a single VeriSign
external binding.  The external binding information is used when a SoftLayer customer logs into the SoftLayer
customer portal to authenticate them against a 3rd party, in this case VeriSign.   The information provided
by the VeriSign external binding data type includes:  * The type of credential * The current state of the
credential ** Enabled ** Disabled ** Locked * The credential's expiration date * The last time the credential
was updated   SoftLayer users with an active external binding will be prohibited from using the API for
security reasons."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_External_Binding_Verisign'

    def deleteObject(self, identifier: int) -> bool:
        """Delete a VeriSign external binding."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'deleteObject', id=identifier)
        return data

    def disable(self, identifier: int, reason: str) -> bool:
        """Disable an external binding."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'disable', reason, id=identifier)
        return data

    def enable(self, identifier: int) -> bool:
        """Enable an external binding."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'enable', id=identifier)
        return data

    def getActivationCodeForMobileClient(self) -> str:
        """Get an activation code that is used for provisioning a mobile credential."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getActivationCodeForMobileClient')
        return data

    def getObject(self, identifier: int) -> 'User_Customer_External_Binding_Verisign':
        """Retrieve a SoftLayer_User_Customer_External_Binding_Verisign record."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_External_Binding_Verisign import User_Customer_External_Binding_Verisign
        return data

    def unlock(self, identifier: int, securityCode: str) -> bool:
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'unlock', securityCode, id=identifier)
        return data

    def validateCredentialId(self, userId: int, externalId: str) -> bool:
        """Validate a VeriSign credential id."""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'validateCredentialId', userId, externalId)
        return data

    def getCredentialExpirationDate(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getCredentialExpirationDate', id=identifier)
        return data

    def getCredentialLastUpdateDate(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getCredentialLastUpdateDate', id=identifier)
        return data

    def getCredentialState(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getCredentialState', id=identifier)
        return data

    def getCredentialType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_User_Customer_External_Binding_Verisign', 'getCredentialType', id=identifier)
        return data
