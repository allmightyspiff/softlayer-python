from SoftLayer.sltypes.User.Customer import User_Customer
from SoftLayer.sltypes.User_Customer import User_Customer
from SoftLayer import BaseClient

class User_Customer_OpenIdConnect(User_Customer):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_OpenIdConnect'

    def activateOpenIdConnectUser(self, verificationCode: str, userInfo: 'User_Customer', iamId: str) -> None:
        """Completes invitation process for an OIDC user initiated by the"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'activateOpenIdConnectUser', verificationCode, userInfo, iamId)
        return data

    def completeInvitationAfterLogin(self, providerType: str, accessToken: str, emailRegistrationCode: str) -> None:
        """Completes invitation processing after logging on an existing OpenIdConnect user identity and return an access
token"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'completeInvitationAfterLogin', providerType, accessToken, emailRegistrationCode)
        return data

    def createObject(self, templateObject: 'User_Customer_OpenIdConnect', password: str, vpnPassword: str) -> 'User_Customer_OpenIdConnect':
        """Create a new user record."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'createObject', templateObject, password, vpnPassword)
        from SoftLayer.sltypes.User_Customer_OpenIdConnect import User_Customer_OpenIdConnect
        return data

    def createOpenIdConnectUserAndCompleteInvitation(self, providerType: str, user: 'User_Customer', password: str, registrationCode: str) -> None:
        """Completes invitation processing when a new OpenIdConnect user must be created."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'createOpenIdConnectUserAndCompleteInvitation', providerType, user, password, registrationCode)
        return data

    def declineInvitation(self, providerType: str, registrationCode: str) -> None:
        """Sets a customer invitation as declined."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'declineInvitation', providerType, registrationCode)
        return data

    def getDefaultAccount(self, identifier: int, providerType: str) -> 'Account':
        """Retrieve the default account for the OpenIdConnect identity that is linked to the current active SoftLayer
user identity."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getDefaultAccount', providerType, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getLoginAccountInfoOpenIdConnect(self, providerType: str, accessToken: str) -> 'Container_User_Customer_OpenIdConnect_LoginAccountInfo':
        """Get account for an active user logging into the SoftLayer customer portal"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getLoginAccountInfoOpenIdConnect', providerType, accessToken)
        from SoftLayer.sltypes.Container_User_Customer_OpenIdConnect_LoginAccountInfo import Container_User_Customer_OpenIdConnect_LoginAccountInfo
        return data

    def getMappedAccounts(self, identifier: int, providerType: str) -> list['Account']:
        """Retrieve a list of all active accounts that belong to this customer."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getMappedAccounts', providerType, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getObject(self, identifier: int) -> 'User_Customer_OpenIdConnect':
        """Retrieve a SoftLayer_User_Customer_OpenIdConnect record."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_OpenIdConnect import User_Customer_OpenIdConnect
        return data

    def getOpenIdRegistrationInfoFromCode(self, providerType: str, registrationCode: str) -> 'Account_Authentication_OpenIdConnect_RegistrationInformation':
        """Get OpenId User Registration details from the provided email code"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getOpenIdRegistrationInfoFromCode', providerType, registrationCode)
        from SoftLayer.sltypes.Account_Authentication_OpenIdConnect_RegistrationInformation import Account_Authentication_OpenIdConnect_RegistrationInformation
        return data

    def getPortalLoginTokenOpenIdConnect(self, providerType: str, accessToken: str, accountId: int, securityQuestionId: int, securityQuestionAnswer: str) -> 'Container_User_Customer_Portal_Token':
        """Authenticate a user for the SoftLayer customer portal via an openIdConnect provider."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getPortalLoginTokenOpenIdConnect', providerType, accessToken, accountId, securityQuestionId, securityQuestionAnswer)
        from SoftLayer.sltypes.Container_User_Customer_Portal_Token import Container_User_Customer_Portal_Token
        return data

    def getRequirementsForPasswordSet(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet') -> 'Container_User_Customer_PasswordSet':
        """Retrieve the authentication requirements for a user when attempting"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getRequirementsForPasswordSet', passwordSet, id=identifier)
        from SoftLayer.sltypes.Container_User_Customer_PasswordSet import Container_User_Customer_PasswordSet
        return data

    def getUserForUnifiedInvitation(self, openIdConnectUserId: str, uniqueIdentifier: str, searchInvitationsNotLinksFlag: str, accountId: str) -> 'User_Customer_OpenIdConnect':
        """Get the IMS User Object for the provided OpenIdConnect User ID, or (Optional) IBMid Unique Identifier."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getUserForUnifiedInvitation', openIdConnectUserId, uniqueIdentifier, searchInvitationsNotLinksFlag, accountId)
        from SoftLayer.sltypes.User_Customer_OpenIdConnect import User_Customer_OpenIdConnect
        return data

    def getUserIdForPasswordSet(self, key: str) -> int:
        """Retrieve a user id using a password request key"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'getUserIdForPasswordSet', key)
        return data

    def initiatePortalPasswordChange(self, username: str) -> bool:
        """Request email to allow user to change their password"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'initiatePortalPasswordChange', username)
        return data

    def initiatePortalPasswordChangeByBrandAgent(self, identifier: int, username: str) -> bool:
        """Allows a Brand Agent to request password reset email to be sent to"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'initiatePortalPasswordChangeByBrandAgent', username, id=identifier)
        return data

    def isValidPortalPassword(self, identifier: int, password: str) -> bool:
        """Determine if a string is a user's portal password."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'isValidPortalPassword', password, id=identifier)
        return data

    def processPasswordSetRequest(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet', authenticationContainer: 'Container_User_Customer_External_Binding') -> bool:
        """Set the password for a user who has a valid password request key"""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'processPasswordSetRequest', passwordSet, authenticationContainer, id=identifier)
        return data

    def selfPasswordChange(self, identifier: int, currentPassword: str, newPassword: str) -> None:
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'selfPasswordChange', currentPassword, newPassword, id=identifier)
        return data

    def setDefaultAccount(self, identifier: int, providerType: str, accountId: int) -> 'Account':
        """Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user
identity."""
        data = self.client.call('SoftLayer_User_Customer_OpenIdConnect', 'setDefaultAccount', providerType, accountId, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data
