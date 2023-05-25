from datetime import datetime
from SoftLayer.sltypes.Container.User.Authentication.Token import Container_User_Authentication_Token
from SoftLayer.sltypes.User.Interface import User_Interface
from SoftLayer.sltypes.User_Interface import User_Interface
from SoftLayer import BaseClient

class User_Customer(User_Interface):
    """The SoftLayer_User_Customer data type contains general information relating to a single SoftLayer customer
portal user. Personal information in this type such as names, addresses, and phone numbers are not
necessarily associated with the customer account the user is assigned to."""
    accountId: int
    address1: str
    address2: str
    aim: str
    alternatePhone: str
    authenticationToken: Container_User_Authentication_Token
    city: str
    companyName: str
    country: str
    createDate: datetime
    daylightSavingsTimeFlag: bool
    denyAllResourceAccessOnCreateFlag: bool
    displayName: str
    email: str
    firstName: str
    forumPasswordHash: str
    iamAuthorizationStatus: int
    iamId: str
    icq: str
    id_: int
    ipAddressRestriction: str
    isMasterUserFlag: bool
    lastName: str
    linkedAccountIntegrationMode: str
    localeId: int
    managedByFederationFlag: bool
    managedByOpenIdConnectFlag: bool
    minimumPasswordLifeHours: int
    modifyDate: datetime
    msn: str
    nameId: str
    officePhone: str
    openIdConnectUserName: str
    parentId: int
    passwordExpireDate: datetime
    permissionCheckLikeMasterUserFlag: int
    postalCode: str
    pptpVpnAllowedFlag: bool
    preventPreviousPasswords: int
    savedId: str
    secondaryLoginManagementFlag: bool
    secondaryLoginRequiredFlag: bool
    secondaryPasswordModifyDate: datetime
    secondaryPasswordTimeoutDays: int
    sms: str
    sslVpnAllowedFlag: bool
    state: str
    statusDate: datetime
    timezoneId: int
    userStatusId: int
    username: str
    verificationCode: str
    vpnManualConfig: bool
    yahoo: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer'

    def acknowledgeSupportPolicy(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_User_Customer', 'acknowledgeSupportPolicy', id=identifier)
        return data

    def addApiAuthenticationKey(self, identifier: int) -> str:
        """Create a user's API authentication key."""
        data = self.client.call('SoftLayer_User_Customer', 'addApiAuthenticationKey', id=identifier)
        return data

    def addBulkDedicatedHostAccess(self, identifier: int, dedicatedHostIds: int) -> bool:
        """Grant access to the user for one or more dedicated hosts devices."""
        data = self.client.call('SoftLayer_User_Customer', 'addBulkDedicatedHostAccess', dedicatedHostIds, id=identifier)
        return data

    def addBulkHardwareAccess(self, identifier: int, hardwareIds: int) -> bool:
        """Add multiple hardware to a portal user's hardware access list."""
        data = self.client.call('SoftLayer_User_Customer', 'addBulkHardwareAccess', hardwareIds, id=identifier)
        return data

    def addBulkPortalPermission(self, identifier: int, permissions: 'User_Customer_CustomerPermission_Permission') -> bool:
        """Add multiple permissions to a portal user's permission set."""
        data = self.client.call('SoftLayer_User_Customer', 'addBulkPortalPermission', permissions, id=identifier)
        return data

    def addBulkRoles(self, identifier: int, roles: 'User_Permission_Role') -> None:
        data = self.client.call('SoftLayer_User_Customer', 'addBulkRoles', roles, id=identifier)
        return data

    def addBulkVirtualGuestAccess(self, identifier: int, virtualGuestIds: int) -> bool:
        """Add multiple CloudLayer Computing Instances to a portal user's access list."""
        data = self.client.call('SoftLayer_User_Customer', 'addBulkVirtualGuestAccess', virtualGuestIds, id=identifier)
        return data

    def addDedicatedHostAccess(self, identifier: int, dedicatedHostId: int) -> bool:
        """Grant access to the user for a single dedicated host device."""
        data = self.client.call('SoftLayer_User_Customer', 'addDedicatedHostAccess', dedicatedHostId, id=identifier)
        return data

    def addExternalBinding(self, identifier: int, externalBinding: 'User_External_Binding') -> 'User_Customer_External_Binding':
        data = self.client.call('SoftLayer_User_Customer', 'addExternalBinding', externalBinding, id=identifier)
        from SoftLayer.sltypes.User_Customer_External_Binding import User_Customer_External_Binding
        return data

    def addHardwareAccess(self, identifier: int, hardwareId: int) -> bool:
        """Add hardware to a portal user's hardware access list."""
        data = self.client.call('SoftLayer_User_Customer', 'addHardwareAccess', hardwareId, id=identifier)
        return data

    def addNotificationSubscriber(self, identifier: int, notificationKeyName: str) -> bool:
        """Create a notification subscription record for the user."""
        data = self.client.call('SoftLayer_User_Customer', 'addNotificationSubscriber', notificationKeyName, id=identifier)
        return data

    def addPortalPermission(self, identifier: int, permission: 'User_Customer_CustomerPermission_Permission') -> bool:
        """Add a permission to a portal user's permission set."""
        data = self.client.call('SoftLayer_User_Customer', 'addPortalPermission', permission, id=identifier)
        return data

    def addRole(self, identifier: int, role: 'User_Permission_Role') -> None:
        data = self.client.call('SoftLayer_User_Customer', 'addRole', role, id=identifier)
        return data

    def addVirtualGuestAccess(self, identifier: int, virtualGuestId: int) -> bool:
        """Add a CloudLayer Computing Instance to a portal user's access list."""
        data = self.client.call('SoftLayer_User_Customer', 'addVirtualGuestAccess', virtualGuestId, id=identifier)
        return data

    def assignNewParentId(self, identifier: int, parentId: int, cascadePermissionsFlag: bool) -> 'User_Customer':
        """Assign a different parent to this user."""
        data = self.client.call('SoftLayer_User_Customer', 'assignNewParentId', parentId, cascadePermissionsFlag, id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def changePreference(self, identifier: int, preferenceTypeKeyName: str, value: str) -> list['User_Preference']:
        """Change preference values for the current user"""
        data = self.client.call('SoftLayer_User_Customer', 'changePreference', preferenceTypeKeyName, value, id=identifier)
        from SoftLayer.sltypes.User_Preference import User_Preference
        return data

    def createNotificationSubscriber(self, identifier: int, keyName: str, resourceTableId: int) -> bool:
        """Create a new subscriber for a given resource."""
        data = self.client.call('SoftLayer_User_Customer', 'createNotificationSubscriber', keyName, resourceTableId, id=identifier)
        return data

    def createObject(self, templateObject: 'User_Customer', password: str, vpnPassword: str) -> 'User_Customer':
        """Create a new user record."""
        data = self.client.call('SoftLayer_User_Customer', 'createObject', templateObject, password, vpnPassword)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def createSubscriberDeliveryMethods(self, identifier: int, notificationKeyName: str, deliveryMethodKeyNames: str) -> bool:
        """Create delivery methods for the subscriber."""
        data = self.client.call('SoftLayer_User_Customer', 'createSubscriberDeliveryMethods', notificationKeyName, deliveryMethodKeyNames, id=identifier)
        return data

    def deactivateNotificationSubscriber(self, identifier: int, keyName: str, resourceTableId: int) -> bool:
        """Delete a subscriber for a given resource."""
        data = self.client.call('SoftLayer_User_Customer', 'deactivateNotificationSubscriber', keyName, resourceTableId, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'User_Customer') -> bool:
        """Update a user's information."""
        data = self.client.call('SoftLayer_User_Customer', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'User_Customer') -> bool:
        """Update a collection of users' information"""
        data = self.client.call('SoftLayer_User_Customer', 'editObjects', templateObjects)
        return data

    def findUserPreference(self, identifier: int, profileName: str, containerKeyname: str, preferenceKeyname: str) -> list['Layout_Profile']:
        data = self.client.call('SoftLayer_User_Customer', 'findUserPreference', profileName, containerKeyname, preferenceKeyname, id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data

    def getActiveExternalAuthenticationVendors(self) -> list['Container_User_Customer_External_Binding_Vendor']:
        """Get a list of active external authentication vendors for a SoftLayer user."""
        data = self.client.call('SoftLayer_User_Customer', 'getActiveExternalAuthenticationVendors')
        from SoftLayer.sltypes.Container_User_Customer_External_Binding_Vendor import Container_User_Customer_External_Binding_Vendor
        return data

    def getAgentImpersonationToken(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'getAgentImpersonationToken', id=identifier)
        return data

    def getAllowedDedicatedHostIds(self, identifier: int) -> list[int]:
        data = self.client.call('SoftLayer_User_Customer', 'getAllowedDedicatedHostIds', id=identifier)
        return data

    def getAllowedHardwareIds(self, identifier: int) -> list[int]:
        data = self.client.call('SoftLayer_User_Customer', 'getAllowedHardwareIds', id=identifier)
        return data

    def getAllowedVirtualGuestIds(self, identifier: int) -> list[int]:
        data = self.client.call('SoftLayer_User_Customer', 'getAllowedVirtualGuestIds', id=identifier)
        return data

    def getAuthenticationToken(self, identifier: int, token: 'Container_User_Authentication_Token') -> 'Container_User_Authentication_Token':
        """Generate a specific type of authentication token"""
        data = self.client.call('SoftLayer_User_Customer', 'getAuthenticationToken', token, id=identifier)
        from SoftLayer.sltypes.Container_User_Authentication_Token import Container_User_Authentication_Token
        return data

    def getDefaultAccount(self, identifier: int, providerType: str) -> 'Account':
        """This method should never be invoked as it is not applicable to legacy SoftLayer-authenticated users. See
SoftLayer_User_Customer_OpenIdConnect::getDefaultAccount instead."""
        data = self.client.call('SoftLayer_User_Customer', 'getDefaultAccount', providerType, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getHardwareCount(self, identifier: int) -> int:
        """Retrieve the current number of servers a portal user has access to."""
        data = self.client.call('SoftLayer_User_Customer', 'getHardwareCount', id=identifier)
        return data

    def getImpersonationToken(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'getImpersonationToken', id=identifier)
        return data

    def getLoginToken(self, request: 'Container_Authentication_Request_Contract') -> 'Container_Authentication_Response_Common':
        """Authenticate a user for the SoftLayer customer portal"""
        data = self.client.call('SoftLayer_User_Customer', 'getLoginToken', request)
        from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common
        return data

    def getMappedAccounts(self, identifier: int, providerType: str) -> list['Account']:
        """Retrieve a list of all the accounts that belong to this customer."""
        data = self.client.call('SoftLayer_User_Customer', 'getMappedAccounts', providerType, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getObject(self, identifier: int) -> 'User_Customer':
        """Retrieve a SoftLayer_User_Customer record."""
        data = self.client.call('SoftLayer_User_Customer', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getOpenIdConnectMigrationState(self, identifier: int) -> 'Container_User_Customer_OpenIdConnect_MigrationState':
        """Get the OpenId migration state"""
        data = self.client.call('SoftLayer_User_Customer', 'getOpenIdConnectMigrationState', id=identifier)
        from SoftLayer.sltypes.Container_User_Customer_OpenIdConnect_MigrationState import Container_User_Customer_OpenIdConnect_MigrationState
        return data

    def getPasswordRequirements(self, isVpn: bool) -> 'Container_User_Customer_PasswordSet':
        data = self.client.call('SoftLayer_User_Customer', 'getPasswordRequirements', isVpn)
        from SoftLayer.sltypes.Container_User_Customer_PasswordSet import Container_User_Customer_PasswordSet
        return data

    def getPortalLoginToken(self, username: str, password: str, securityQuestionId: int, securityQuestionAnswer: str) -> 'Container_User_Customer_Portal_Token':
        """Authenticate a user for the SoftLayer customer portal"""
        data = self.client.call('SoftLayer_User_Customer', 'getPortalLoginToken', username, password, securityQuestionId, securityQuestionAnswer)
        from SoftLayer.sltypes.Container_User_Customer_Portal_Token import Container_User_Customer_Portal_Token
        return data

    def getPreference(self, identifier: int, preferenceTypeKeyName: str) -> 'User_Preference':
        """Get a preference value for the current user"""
        data = self.client.call('SoftLayer_User_Customer', 'getPreference', preferenceTypeKeyName, id=identifier)
        from SoftLayer.sltypes.User_Preference import User_Preference
        return data

    def getPreferenceTypes(self, identifier: int) -> list['User_Preference_Type']:
        """Get all available preference types"""
        data = self.client.call('SoftLayer_User_Customer', 'getPreferenceTypes', id=identifier)
        from SoftLayer.sltypes.User_Preference_Type import User_Preference_Type
        return data

    def getRequirementsForPasswordSet(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet') -> 'Container_User_Customer_PasswordSet':
        """Retrieve the authentication requirements for a user when attempting"""
        data = self.client.call('SoftLayer_User_Customer', 'getRequirementsForPasswordSet', passwordSet, id=identifier)
        from SoftLayer.sltypes.Container_User_Customer_PasswordSet import Container_User_Customer_PasswordSet
        return data

    def getSupportPolicyDocument(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'getSupportPolicyDocument', id=identifier)
        return data

    def getSupportPolicyName(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'getSupportPolicyName', id=identifier)
        return data

    def getSupportedLocales(self, identifier: int) -> list['Locale']:
        """Returns all supported locales for the current user"""
        data = self.client.call('SoftLayer_User_Customer', 'getSupportedLocales', id=identifier)
        from SoftLayer.sltypes.Locale import Locale
        return data

    def getUserIdForPasswordSet(self, key: str) -> int:
        """Retrieve a user id using a password request key"""
        data = self.client.call('SoftLayer_User_Customer', 'getUserIdForPasswordSet', key)
        return data

    def getUserPreferences(self, identifier: int, profileName: str, containerKeyname: str) -> list['Layout_Profile']:
        data = self.client.call('SoftLayer_User_Customer', 'getUserPreferences', profileName, containerKeyname, id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data

    def getVirtualGuestCount(self, identifier: int) -> int:
        """Retrieve the current number of CloudLayer Computing Instances a portal user has access to."""
        data = self.client.call('SoftLayer_User_Customer', 'getVirtualGuestCount', id=identifier)
        return data

    def inTerminalStatus(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_User_Customer', 'inTerminalStatus', id=identifier)
        return data

    def initiatePortalPasswordChange(self, username: str) -> bool:
        """Request email to allow user to change their password"""
        data = self.client.call('SoftLayer_User_Customer', 'initiatePortalPasswordChange', username)
        return data

    def initiatePortalPasswordChangeByBrandAgent(self, identifier: int, username: str) -> bool:
        """Allows a Brand Agent to request password reset email to be sent to"""
        data = self.client.call('SoftLayer_User_Customer', 'initiatePortalPasswordChangeByBrandAgent', username, id=identifier)
        return data

    def inviteUserToLinkOpenIdConnect(self, identifier: int, providerType: str) -> None:
        """Send email invitation to a user to join a SoftLayer account and authenticate with OpenIdConnect."""
        data = self.client.call('SoftLayer_User_Customer', 'inviteUserToLinkOpenIdConnect', providerType, id=identifier)
        return data

    def isMasterUser(self, identifier: int) -> bool:
        """Determine if a portal user is a master user."""
        data = self.client.call('SoftLayer_User_Customer', 'isMasterUser', id=identifier)
        return data

    def isValidPortalPassword(self, identifier: int, password: str) -> bool:
        """Determine if a string is a user's portal password."""
        data = self.client.call('SoftLayer_User_Customer', 'isValidPortalPassword', password, id=identifier)
        return data

    def performExternalAuthentication(self, authenticationContainer: 'Container_User_Customer_External_Binding') -> 'Container_User_Customer_Portal_Token':
        """Perform an external authentication using the given authentication container."""
        data = self.client.call('SoftLayer_User_Customer', 'performExternalAuthentication', authenticationContainer)
        from SoftLayer.sltypes.Container_User_Customer_Portal_Token import Container_User_Customer_Portal_Token
        return data

    def processPasswordSetRequest(self, identifier: int, passwordSet: 'Container_User_Customer_PasswordSet', authenticationContainer: 'Container_User_Customer_External_Binding') -> bool:
        """Set the password for a user who has a valid password request key"""
        data = self.client.call('SoftLayer_User_Customer', 'processPasswordSetRequest', passwordSet, authenticationContainer, id=identifier)
        return data

    def removeAllDedicatedHostAccessForThisUser(self, identifier: int) -> bool:
        """Revoke access to all dedicated hosts on the account for this user."""
        data = self.client.call('SoftLayer_User_Customer', 'removeAllDedicatedHostAccessForThisUser', id=identifier)
        return data

    def removeAllHardwareAccessForThisUser(self, identifier: int) -> bool:
        """Remove all hardware from a portal user's hardware access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeAllHardwareAccessForThisUser', id=identifier)
        return data

    def removeAllVirtualAccessForThisUser(self, identifier: int) -> bool:
        """Remove all cloud computing instances from a portal user's instance access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeAllVirtualAccessForThisUser', id=identifier)
        return data

    def removeApiAuthenticationKey(self, keyId: int) -> bool:
        """Remove a user's API authentication key."""
        data = self.client.call('SoftLayer_User_Customer', 'removeApiAuthenticationKey', keyId)
        return data

    def removeBulkDedicatedHostAccess(self, identifier: int, dedicatedHostIds: int) -> bool:
        """Revoke access for the user for one or more dedicated hosts devices."""
        data = self.client.call('SoftLayer_User_Customer', 'removeBulkDedicatedHostAccess', dedicatedHostIds, id=identifier)
        return data

    def removeBulkHardwareAccess(self, identifier: int, hardwareIds: int) -> bool:
        """Remove multiple hardware from a portal user's hardware access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeBulkHardwareAccess', hardwareIds, id=identifier)
        return data

    def removeBulkPortalPermission(self, identifier: int, permissions: 'User_Customer_CustomerPermission_Permission', cascadePermissionsFlag: bool) -> bool:
        """Remove multiple permissions from a portal user's permission set."""
        data = self.client.call('SoftLayer_User_Customer', 'removeBulkPortalPermission', permissions, cascadePermissionsFlag, id=identifier)
        return data

    def removeBulkRoles(self, identifier: int, roles: 'User_Permission_Role') -> None:
        data = self.client.call('SoftLayer_User_Customer', 'removeBulkRoles', roles, id=identifier)
        return data

    def removeBulkVirtualGuestAccess(self, identifier: int, virtualGuestIds: int) -> bool:
        """Remove multiple CloudLayer Computing Instances from a portal user's access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeBulkVirtualGuestAccess', virtualGuestIds, id=identifier)
        return data

    def removeDedicatedHostAccess(self, identifier: int, dedicatedHostId: int) -> bool:
        """Revoke access for the user to a single dedicated hosts device."""
        data = self.client.call('SoftLayer_User_Customer', 'removeDedicatedHostAccess', dedicatedHostId, id=identifier)
        return data

    def removeExternalBinding(self, identifier: int, externalBinding: 'User_External_Binding') -> bool:
        """Remove an external binding from this user."""
        data = self.client.call('SoftLayer_User_Customer', 'removeExternalBinding', externalBinding, id=identifier)
        return data

    def removeHardwareAccess(self, identifier: int, hardwareId: int) -> bool:
        """Remove hardware from a portal user's hardware access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeHardwareAccess', hardwareId, id=identifier)
        return data

    def removePortalPermission(self, identifier: int, permission: 'User_Customer_CustomerPermission_Permission', cascadePermissionsFlag: bool) -> bool:
        """Remove a permission from a portal user's permission set."""
        data = self.client.call('SoftLayer_User_Customer', 'removePortalPermission', permission, cascadePermissionsFlag, id=identifier)
        return data

    def removeRole(self, identifier: int, role: 'User_Permission_Role') -> None:
        data = self.client.call('SoftLayer_User_Customer', 'removeRole', role, id=identifier)
        return data

    def removeSecurityAnswers(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_User_Customer', 'removeSecurityAnswers', id=identifier)
        return data

    def removeVirtualGuestAccess(self, identifier: int, virtualGuestId: int) -> bool:
        """Remove a CloudLayer Computing Instance from a portal user's access list."""
        data = self.client.call('SoftLayer_User_Customer', 'removeVirtualGuestAccess', virtualGuestId, id=identifier)
        return data

    def resetOpenIdConnectLink(self, identifier: int, providerType: str, newIbmIdUsername: str, removeSecuritySettings: bool) -> None:
        """Change the link of a user for OpenIdConnect managed accounts, provided the"""
        data = self.client.call('SoftLayer_User_Customer', 'resetOpenIdConnectLink', providerType, newIbmIdUsername, removeSecuritySettings, id=identifier)
        return data

    def resetOpenIdConnectLinkUnifiedUserManagementMode(self, identifier: int, providerType: str, newIbmIdUsername: str, removeSecuritySettings: bool) -> None:
        """Change the link of a master user for OpenIdConnect managed accounts,"""
        data = self.client.call('SoftLayer_User_Customer', 'resetOpenIdConnectLinkUnifiedUserManagementMode', providerType, newIbmIdUsername, removeSecuritySettings, id=identifier)
        return data

    def samlAuthenticate(self, accountId: str, samlResponse: str) -> 'Container_User_Customer_Portal_Token':
        data = self.client.call('SoftLayer_User_Customer', 'samlAuthenticate', accountId, samlResponse)
        from SoftLayer.sltypes.Container_User_Customer_Portal_Token import Container_User_Customer_Portal_Token
        return data

    def samlBeginAuthentication(self, accountId: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'samlBeginAuthentication', accountId)
        return data

    def samlBeginLogout(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_User_Customer', 'samlBeginLogout', id=identifier)
        return data

    def samlLogout(self, identifier: int, samlResponse: str) -> None:
        data = self.client.call('SoftLayer_User_Customer', 'samlLogout', samlResponse, id=identifier)
        return data

    def selfPasswordChange(self, identifier: int, currentPassword: str, newPassword: str) -> None:
        data = self.client.call('SoftLayer_User_Customer', 'selfPasswordChange', currentPassword, newPassword, id=identifier)
        return data

    def setDefaultAccount(self, identifier: int, providerType: str, accountId: int) -> 'Account':
        """Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user
identity."""
        data = self.client.call('SoftLayer_User_Customer', 'setDefaultAccount', providerType, accountId, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def silentlyMigrateUserOpenIdConnect(self, identifier: int, providerType: str) -> bool:
        """This api is used to migrate a user to IBMid without sending an invitation."""
        data = self.client.call('SoftLayer_User_Customer', 'silentlyMigrateUserOpenIdConnect', providerType, id=identifier)
        return data

    def turnOffMasterUserPermissionCheckMode(self, identifier: int) -> None:
        """De-activates the behavior that IMS permission checks for this user will be"""
        data = self.client.call('SoftLayer_User_Customer', 'turnOffMasterUserPermissionCheckMode', id=identifier)
        return data

    def turnOnMasterUserPermissionCheckMode(self, identifier: int) -> None:
        """Activates the behavior that IMS permission checks for this user will be done as though"""
        data = self.client.call('SoftLayer_User_Customer', 'turnOnMasterUserPermissionCheckMode', id=identifier)
        return data

    def updateNotificationSubscriber(self, identifier: int, notificationKeyName: str, active: int) -> bool:
        """Update the active status for a notification subscription."""
        data = self.client.call('SoftLayer_User_Customer', 'updateNotificationSubscriber', notificationKeyName, active, id=identifier)
        return data

    def updateSecurityAnswers(self, identifier: int, questions: 'User_Security_Question', answers: str) -> bool:
        """Update portal login security questions and answers."""
        data = self.client.call('SoftLayer_User_Customer', 'updateSecurityAnswers', questions, answers, id=identifier)
        return data

    def updateSubscriberDeliveryMethod(self, identifier: int, notificationKeyName: str, deliveryMethodKeyNames: str, active: int) -> bool:
        """Update a delivery method for the subscriber."""
        data = self.client.call('SoftLayer_User_Customer', 'updateSubscriberDeliveryMethod', notificationKeyName, deliveryMethodKeyNames, active, id=identifier)
        return data

    def updateVpnPassword(self, identifier: int, password: str) -> bool:
        """Update a user's VPN password"""
        data = self.client.call('SoftLayer_User_Customer', 'updateVpnPassword', password, id=identifier)
        return data

    def updateVpnUser(self, identifier: int) -> bool:
        """Creates or updates a user's VPN access privileges."""
        data = self.client.call('SoftLayer_User_Customer', 'updateVpnUser', id=identifier)
        return data

    def validateAuthenticationToken(self, authenticationToken: 'Container_User_Authentication_Token') -> 'Container_User_Customer_Portal_Token':
        """Validate the user authentication token"""
        data = self.client.call('SoftLayer_User_Customer', 'validateAuthenticationToken', authenticationToken)
        from SoftLayer.sltypes.Container_User_Customer_Portal_Token import Container_User_Customer_Portal_Token
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActions(self, identifier: int) -> list['User_Permission_Action']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getActions', id=identifier)
        from SoftLayer.sltypes.User_Permission_Action import User_Permission_Action
        return data

    def getAdditionalEmails(self, identifier: int) -> list['User_Customer_AdditionalEmail']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getAdditionalEmails', id=identifier)
        from SoftLayer.sltypes.User_Customer_AdditionalEmail import User_Customer_AdditionalEmail
        return data

    def getApiAuthenticationKeys(self, identifier: int) -> list['User_Customer_ApiAuthentication']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getApiAuthenticationKeys', id=identifier)
        from SoftLayer.sltypes.User_Customer_ApiAuthentication import User_Customer_ApiAuthentication
        return data

    def getChildUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getChildUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getClosedTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getClosedTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getDedicatedHosts(self, identifier: int) -> list['Virtual_DedicatedHost']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getDedicatedHosts', id=identifier)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data

    def getExternalBindings(self, identifier: int) -> list['User_External_Binding']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getExternalBindings', id=identifier)
        from SoftLayer.sltypes.User_External_Binding import User_External_Binding
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareNotifications(self, identifier: int) -> list['User_Customer_Notification_Hardware']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHardwareNotifications', id=identifier)
        from SoftLayer.sltypes.User_Customer_Notification_Hardware import User_Customer_Notification_Hardware
        return data

    def getHasAcknowledgedSupportPolicyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHasAcknowledgedSupportPolicyFlag', id=identifier)
        return data

    def getHasFullDedicatedHostAccessFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHasFullDedicatedHostAccessFlag', id=identifier)
        return data

    def getHasFullHardwareAccessFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHasFullHardwareAccessFlag', id=identifier)
        return data

    def getHasFullVirtualGuestAccessFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getHasFullVirtualGuestAccessFlag', id=identifier)
        return data

    def getIbmIdLink(self, identifier: int) -> 'User_Customer_Link':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getIbmIdLink', id=identifier)
        from SoftLayer.sltypes.User_Customer_Link import User_Customer_Link
        return data

    def getLayoutProfiles(self, identifier: int) -> list['Layout_Profile']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getLayoutProfiles', id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data

    def getLocale(self, identifier: int) -> 'Locale':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getLocale', id=identifier)
        from SoftLayer.sltypes.Locale import Locale
        return data

    def getLoginAttempts(self, identifier: int) -> list['User_Customer_Access_Authentication']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getLoginAttempts', id=identifier)
        from SoftLayer.sltypes.User_Customer_Access_Authentication import User_Customer_Access_Authentication
        return data

    def getMobileDevices(self, identifier: int) -> list['User_Customer_MobileDevice']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getMobileDevices', id=identifier)
        from SoftLayer.sltypes.User_Customer_MobileDevice import User_Customer_MobileDevice
        return data

    def getNotificationSubscribers(self, identifier: int) -> list['Notification_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getNotificationSubscribers', id=identifier)
        from SoftLayer.sltypes.Notification_Subscriber import Notification_Subscriber
        return data

    def getOpenTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getOpenTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOverrides(self, identifier: int) -> list['Network_Service_Vpn_Overrides']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getOverrides', id=identifier)
        from SoftLayer.sltypes.Network_Service_Vpn_Overrides import Network_Service_Vpn_Overrides
        return data

    def getParent(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getParent', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getPermissions(self, identifier: int) -> list['User_Customer_CustomerPermission_Permission']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getPermissions', id=identifier)
        from SoftLayer.sltypes.User_Customer_CustomerPermission_Permission import User_Customer_CustomerPermission_Permission
        return data

    def getPreferences(self, identifier: int) -> list['User_Preference']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getPreferences', id=identifier)
        from SoftLayer.sltypes.User_Preference import User_Preference
        return data

    def getRoles(self, identifier: int) -> list['User_Permission_Role']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getRoles', id=identifier)
        from SoftLayer.sltypes.User_Permission_Role import User_Permission_Role
        return data

    def getSecurityAnswers(self, identifier: int) -> list['User_Customer_Security_Answer']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSecurityAnswers', id=identifier)
        from SoftLayer.sltypes.User_Customer_Security_Answer import User_Customer_Security_Answer
        return data

    def getSubscribers(self, identifier: int) -> list['Notification_User_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSubscribers', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
        return data

    def getSuccessfulLogins(self, identifier: int) -> list['User_Customer_Access_Authentication']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSuccessfulLogins', id=identifier)
        from SoftLayer.sltypes.User_Customer_Access_Authentication import User_Customer_Access_Authentication
        return data

    def getSupportPolicyAcknowledgementRequiredFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSupportPolicyAcknowledgementRequiredFlag', id=identifier)
        return data

    def getSurveyRequiredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSurveyRequiredFlag', id=identifier)
        return data

    def getSurveys(self, identifier: int) -> list['Survey']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getSurveys', id=identifier)
        from SoftLayer.sltypes.Survey import Survey
        return data

    def getTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getTimezone(self, identifier: int) -> 'Locale_Timezone':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getTimezone', id=identifier)
        from SoftLayer.sltypes.Locale_Timezone import Locale_Timezone
        return data

    def getUnsuccessfulLogins(self, identifier: int) -> list['User_Customer_Access_Authentication']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getUnsuccessfulLogins', id=identifier)
        from SoftLayer.sltypes.User_Customer_Access_Authentication import User_Customer_Access_Authentication
        return data

    def getUserLinks(self, identifier: int) -> list['User_Customer_Link']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getUserLinks', id=identifier)
        from SoftLayer.sltypes.User_Customer_Link import User_Customer_Link
        return data

    def getUserStatus(self, identifier: int) -> 'User_Customer_Status':
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getUserStatus', id=identifier)
        from SoftLayer.sltypes.User_Customer_Status import User_Customer_Status
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_User_Customer', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
