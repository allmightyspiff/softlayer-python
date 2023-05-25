from SoftLayer.sltypes.User.Customer.OpenIdConnect import User_Customer_OpenIdConnect
from SoftLayer.sltypes.User_Customer_OpenIdConnect import User_Customer_OpenIdConnect
from SoftLayer import BaseClient

class User_Customer_OpenIdConnect_TrustedProfile(User_Customer_OpenIdConnect):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_OpenIdConnect_TrustedProfile'

    def addApiAuthenticationKey(self, identifier: int) -> str:
        """Create a user's API authentication key."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'addApiAuthenticationKey', id=identifier)
        return data

    def addExternalBinding(self, identifier: int, externalBinding: 'User_External_Binding') -> 'User_Customer_External_Binding':
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'addExternalBinding', externalBinding, id=identifier)
        from SoftLayer.sltypes.User_Customer_External_Binding import User_Customer_External_Binding
        return data

    def createObject(self, templateObject: 'User_Customer_OpenIdConnect_TrustedProfile', password: str, vpnPassword: str) -> 'User_Customer_OpenIdConnect_TrustedProfile':
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'createObject', templateObject, password, vpnPassword)
        return data

    def getLoginToken(self, request: 'Container_Authentication_Request_Contract') -> 'Container_Authentication_Response_Common':
        """Authenticate a user for the SoftLayer customer portal"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'getLoginToken', request)
        from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common
        return data

    def getObject(self, identifier: int) -> 'User_Customer_OpenIdConnect_TrustedProfile':
        """Retrieve a SoftLayer_User_Customer_OpenIdConnect_TrustedProfile record."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'getObject', id=identifier)
        return data

    def getRequirementsForPasswordSet(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet') -> 'Container_User_Customer_PasswordSet':
        """Retrieve the authentication requirements for a user when attempting"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'getRequirementsForPasswordSet', passwordSet, id=identifier)
        from SoftLayer.sltypes.Container_User_Customer_PasswordSet import Container_User_Customer_PasswordSet
        return data

    def getUserIdForPasswordSet(self, key: str) -> int:
        """Retrieve a user id using a password request key"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'getUserIdForPasswordSet', key)
        return data

    def initiatePortalPasswordChange(self, username: str) -> bool:
        """Request email to allow user to change their password"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'initiatePortalPasswordChange', username)
        return data

    def initiatePortalPasswordChangeByBrandAgent(self, identifier: int, username: str) -> bool:
        """Allows a Brand Agent to request password reset email to be sent to"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'initiatePortalPasswordChangeByBrandAgent', username, id=identifier)
        return data

    def isValidPortalPassword(self, identifier: int, password: str) -> bool:
        """Determine if a string is a user's portal password."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'isValidPortalPassword', password, id=identifier)
        return data

    def processPasswordSetRequest(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet', authenticationContainer: 'Container_User_Customer_External_Binding') -> bool:
        """Set the password for a user who has a valid password request key"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'processPasswordSetRequest', passwordSet, authenticationContainer, id=identifier)
        return data

    def turnOffMasterUserPermissionCheckMode(self, identifier: int) -> None:
        """De-activates the behavior that IMS permission checks for this user will be done as though this was the master
user."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'turnOffMasterUserPermissionCheckMode', id=identifier)
        return data

    def turnOnMasterUserPermissionCheckMode(self, identifier: int) -> None:
        """Activates the behavior that IMS permission checks for this user will be done as though this was the master
user."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'turnOnMasterUserPermissionCheckMode', id=identifier)
        return data

    def updateVpnUser(self, identifier: int) -> bool:
        """Creates or updates a user's VPN access privileges."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect_TrustedProfile', 'updateVpnUser', id=identifier)
        return data
