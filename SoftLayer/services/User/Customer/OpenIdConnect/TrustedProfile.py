# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_OpenIdConnect_TrustedProfile(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_OpenIdConnect_TrustedProfile'
        self.client = client

    def addApiAuthenticationKey(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'addApiAuthenticationKey',
            
        )
        
        return data


    def addExternalBinding(
        self,
        externalBinding: SoftLayer_User_External_Binding,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_External_Binding':

        data = self.client.call(
            self.service,
            'addExternalBinding',
            externalBinding,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.External.Binding import Binding
        return Binding(data)


    def createObject(
        self,
        templateObject: SoftLayer_User_Customer_OpenIdConnect_TrustedProfile,
        password: str,
        vpnPassword: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_OpenIdConnect_TrustedProfile':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            password,
            vpnPassword,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.OpenIdConnect.TrustedProfile import TrustedProfile
        return TrustedProfile(data)


    def getLoginToken(
        self,
        request: SoftLayer_Container_Authentication_Request_Contract
    ) -> 'SoftLayer_Container_Authentication_Response_Common':

        data = self.client.call(
            self.service,
            'getLoginToken',
            request
        )
        from SoftLayer.datatypes.Container.Authentication.Response.Common import Common
        return Common(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_OpenIdConnect_TrustedProfile':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.OpenIdConnect.TrustedProfile import TrustedProfile
        return TrustedProfile(data)


    def getRequirementsForPasswordSet(
        self,
        passwordSet: SoftLayer_Container_User_Customer_PasswordSet
    ) -> 'SoftLayer_Container_User_Customer_PasswordSet':

        data = self.client.call(
            self.service,
            'getRequirementsForPasswordSet',
            passwordSet
        )
        from SoftLayer.datatypes.Container.User.Customer.PasswordSet import PasswordSet
        return PasswordSet(data)


    def getUserIdForPasswordSet(
        self,
        key: str
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getUserIdForPasswordSet',
            key
        )
        
        return data


    def initiatePortalPasswordChange(
        self,
        username: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'initiatePortalPasswordChange',
            username
        )
        
        return data


    def initiatePortalPasswordChangeByBrandAgent(
        self,
        username: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'initiatePortalPasswordChangeByBrandAgent',
            username
        )
        
        return data


    def isValidPortalPassword(
        self,
        password: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isValidPortalPassword',
            password
        )
        
        return data


    def processPasswordSetRequest(
        self,
        passwordSet: SoftLayer_Container_User_Customer_PasswordSet,
        authenticationContainer: SoftLayer_Container_User_Customer_External_Binding
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'processPasswordSetRequest',
            passwordSet,
            authenticationContainer
        )
        
        return data


    def turnOffMasterUserPermissionCheckMode(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'turnOffMasterUserPermissionCheckMode',
            
        )
        
        return data


    def turnOnMasterUserPermissionCheckMode(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'turnOnMasterUserPermissionCheckMode',
            
        )
        
        return data


    def updateVpnUser(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateVpnUser',
            
        )
        
        return data


    def activateOpenIdConnectUser(
        self,
        verificationCode: str,
        userInfo: SoftLayer_User_Customer,
        iamId: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'activateOpenIdConnectUser',
            verificationCode,
            userInfo,
            iamId
        )
        
        return data


    def completeInvitationAfterLogin(
        self,
        providerType: str,
        accessToken: str,
        emailRegistrationCode: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'completeInvitationAfterLogin',
            providerType,
            accessToken,
            emailRegistrationCode
        )
        
        return data


    def createOpenIdConnectUserAndCompleteInvitation(
        self,
        providerType: str,
        user: SoftLayer_User_Customer,
        password: str,
        registrationCode: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'createOpenIdConnectUserAndCompleteInvitation',
            providerType,
            user,
            password,
            registrationCode
        )
        
        return data


    def declineInvitation(
        self,
        providerType: str,
        registrationCode: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'declineInvitation',
            providerType,
            registrationCode
        )
        
        return data


    def getDefaultAccount(
        self,
        providerType: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getDefaultAccount',
            providerType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getLoginAccountInfoOpenIdConnect(
        self,
        providerType: str,
        accessToken: str
    ) -> 'SoftLayer_Container_User_Customer_OpenIdConnect_LoginAccountInfo':

        data = self.client.call(
            self.service,
            'getLoginAccountInfoOpenIdConnect',
            providerType,
            accessToken
        )
        from SoftLayer.datatypes.Container.User.Customer.OpenIdConnect.LoginAccountInfo import LoginAccountInfo
        return LoginAccountInfo(data)


    def getMappedAccounts(
        self,
        providerType: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account]':

        data = self.client.call(
            self.service,
            'getMappedAccounts',
            providerType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getOpenIdRegistrationInfoFromCode(
        self,
        providerType: str,
        registrationCode: str
    ) -> 'SoftLayer_Account_Authentication_OpenIdConnect_RegistrationInformation':

        data = self.client.call(
            self.service,
            'getOpenIdRegistrationInfoFromCode',
            providerType,
            registrationCode
        )
        from SoftLayer.datatypes.Account.Authentication.OpenIdConnect.RegistrationInformation import RegistrationInformation
        return RegistrationInformation(data)


    def getPortalLoginTokenOpenIdConnect(
        self,
        providerType: str,
        accessToken: str,
        accountId: int,
        securityQuestionId: int,
        securityQuestionAnswer: str
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'getPortalLoginTokenOpenIdConnect',
            providerType,
            accessToken,
            accountId,
            securityQuestionId,
            securityQuestionAnswer
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def getUserForUnifiedInvitation(
        self,
        openIdConnectUserId: str,
        uniqueIdentifier: str,
        searchInvitationsNotLinksFlag: str,
        accountId: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_OpenIdConnect':

        data = self.client.call(
            self.service,
            'getUserForUnifiedInvitation',
            openIdConnectUserId,
            uniqueIdentifier,
            searchInvitationsNotLinksFlag,
            accountId,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.OpenIdConnect import OpenIdConnect
        return OpenIdConnect(data)


    def selfPasswordChange(
        self,
        currentPassword: str,
        newPassword: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'selfPasswordChange',
            currentPassword,
            newPassword
        )
        
        return data


    def setDefaultAccount(
        self,
        providerType: str,
        accountId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'setDefaultAccount',
            providerType,
            accountId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def acknowledgeSupportPolicy(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'acknowledgeSupportPolicy',
            
        )
        
        return data


    def addBulkDedicatedHostAccess(
        self,
        dedicatedHostIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkDedicatedHostAccess',
            dedicatedHostIds
        )
        
        return data


    def addBulkHardwareAccess(
        self,
        hardwareIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkHardwareAccess',
            hardwareIds
        )
        
        return data


    def addBulkPortalPermission(
        self,
        permissions: SoftLayer_User_Customer_CustomerPermission_Permission
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkPortalPermission',
            permissions
        )
        
        return data


    def addBulkRoles(
        self,
        roles: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addBulkRoles',
            roles
        )
        
        return data


    def addBulkVirtualGuestAccess(
        self,
        virtualGuestIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkVirtualGuestAccess',
            virtualGuestIds
        )
        
        return data


    def addDedicatedHostAccess(
        self,
        dedicatedHostId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addDedicatedHostAccess',
            dedicatedHostId
        )
        
        return data


    def addHardwareAccess(
        self,
        hardwareId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addHardwareAccess',
            hardwareId
        )
        
        return data


    def addNotificationSubscriber(
        self,
        notificationKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addNotificationSubscriber',
            notificationKeyName
        )
        
        return data


    def addPortalPermission(
        self,
        permission: SoftLayer_User_Customer_CustomerPermission_Permission
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addPortalPermission',
            permission
        )
        
        return data


    def addRole(
        self,
        role: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addRole',
            role
        )
        
        return data


    def addVirtualGuestAccess(
        self,
        virtualGuestId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addVirtualGuestAccess',
            virtualGuestId
        )
        
        return data


    def assignNewParentId(
        self,
        parentId: int,
        cascadePermissionsFlag: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'assignNewParentId',
            parentId,
            cascadePermissionsFlag,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def changePreference(
        self,
        preferenceTypeKeyName: str,
        value: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Preference]':

        data = self.client.call(
            self.service,
            'changePreference',
            preferenceTypeKeyName,
            value,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def createNotificationSubscriber(
        self,
        keyName: str,
        resourceTableId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createNotificationSubscriber',
            keyName,
            resourceTableId
        )
        
        return data


    def createSubscriberDeliveryMethods(
        self,
        notificationKeyName: str,
        deliveryMethodKeyNames: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createSubscriberDeliveryMethods',
            notificationKeyName,
            deliveryMethodKeyNames
        )
        
        return data


    def deactivateNotificationSubscriber(
        self,
        keyName: str,
        resourceTableId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deactivateNotificationSubscriber',
            keyName,
            resourceTableId
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_User_Customer
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_User_Customer
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def findUserPreference(
        self,
        profileName: str,
        containerKeyname: str,
        preferenceKeyname: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'findUserPreference',
            profileName,
            containerKeyname,
            preferenceKeyname,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def getActiveExternalAuthenticationVendors(
        self,
        
    ) -> 'list[SoftLayer_Container_User_Customer_External_Binding_Vendor]':

        data = self.client.call(
            self.service,
            'getActiveExternalAuthenticationVendors',
            
        )
        from SoftLayer.datatypes.Container.User.Customer.External.Binding.Vendor import Vendor
        return Vendor(data)


    def getAgentImpersonationToken(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAgentImpersonationToken',
            
        )
        
        return data


    def getAllowedDedicatedHostIds(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedDedicatedHostIds',
            
        )
        
        return data


    def getAllowedHardwareIds(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedHardwareIds',
            
        )
        
        return data


    def getAllowedVirtualGuestIds(
        self,
        
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedVirtualGuestIds',
            
        )
        
        return data


    def getAuthenticationToken(
        self,
        token: SoftLayer_Container_User_Authentication_Token
    ) -> 'SoftLayer_Container_User_Authentication_Token':

        data = self.client.call(
            self.service,
            'getAuthenticationToken',
            token
        )
        from SoftLayer.datatypes.Container.User.Authentication.Token import Token
        return Token(data)


    def getHardwareCount(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getHardwareCount',
            
        )
        
        return data


    def getImpersonationToken(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getImpersonationToken',
            
        )
        
        return data


    def getOpenIdConnectMigrationState(
        self,
        
    ) -> 'SoftLayer_Container_User_Customer_OpenIdConnect_MigrationState':

        data = self.client.call(
            self.service,
            'getOpenIdConnectMigrationState',
            
        )
        from SoftLayer.datatypes.Container.User.Customer.OpenIdConnect.MigrationState import MigrationState
        return MigrationState(data)


    def getPasswordRequirements(
        self,
        isVpn: boolean
    ) -> 'SoftLayer_Container_User_Customer_PasswordSet':

        data = self.client.call(
            self.service,
            'getPasswordRequirements',
            isVpn
        )
        from SoftLayer.datatypes.Container.User.Customer.PasswordSet import PasswordSet
        return PasswordSet(data)


    def getPortalLoginToken(
        self,
        username: str,
        password: str,
        securityQuestionId: int,
        securityQuestionAnswer: str
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'getPortalLoginToken',
            username,
            password,
            securityQuestionId,
            securityQuestionAnswer
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def getPreference(
        self,
        preferenceTypeKeyName: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Preference':

        data = self.client.call(
            self.service,
            'getPreference',
            preferenceTypeKeyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def getPreferenceTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Preference_Type]':

        data = self.client.call(
            self.service,
            'getPreferenceTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference.Type import Type
        return Type(data)


    def getSupportPolicyDocument(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getSupportPolicyDocument',
            
        )
        
        return data


    def getSupportPolicyName(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportPolicyName',
            
        )
        
        return data


    def getSupportedLocales(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Locale]':

        data = self.client.call(
            self.service,
            'getSupportedLocales',
            mask=objectMask
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


    def getUserPreferences(
        self,
        profileName: str,
        containerKeyname: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'getUserPreferences',
            profileName,
            containerKeyname,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def getVirtualGuestCount(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getVirtualGuestCount',
            
        )
        
        return data


    def inTerminalStatus(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'inTerminalStatus',
            
        )
        
        return data


    def inviteUserToLinkOpenIdConnect(
        self,
        providerType: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'inviteUserToLinkOpenIdConnect',
            providerType
        )
        
        return data


    def isMasterUser(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isMasterUser',
            
        )
        
        return data


    def performExternalAuthentication(
        self,
        authenticationContainer: SoftLayer_Container_User_Customer_External_Binding
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'performExternalAuthentication',
            authenticationContainer
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def removeAllDedicatedHostAccessForThisUser(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllDedicatedHostAccessForThisUser',
            
        )
        
        return data


    def removeAllHardwareAccessForThisUser(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllHardwareAccessForThisUser',
            
        )
        
        return data


    def removeAllVirtualAccessForThisUser(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllVirtualAccessForThisUser',
            
        )
        
        return data


    def removeApiAuthenticationKey(
        self,
        keyId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeApiAuthenticationKey',
            keyId
        )
        
        return data


    def removeBulkDedicatedHostAccess(
        self,
        dedicatedHostIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkDedicatedHostAccess',
            dedicatedHostIds
        )
        
        return data


    def removeBulkHardwareAccess(
        self,
        hardwareIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkHardwareAccess',
            hardwareIds
        )
        
        return data


    def removeBulkPortalPermission(
        self,
        permissions: SoftLayer_User_Customer_CustomerPermission_Permission,
        cascadePermissionsFlag: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkPortalPermission',
            permissions,
            cascadePermissionsFlag
        )
        
        return data


    def removeBulkRoles(
        self,
        roles: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeBulkRoles',
            roles
        )
        
        return data


    def removeBulkVirtualGuestAccess(
        self,
        virtualGuestIds: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkVirtualGuestAccess',
            virtualGuestIds
        )
        
        return data


    def removeDedicatedHostAccess(
        self,
        dedicatedHostId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeDedicatedHostAccess',
            dedicatedHostId
        )
        
        return data


    def removeExternalBinding(
        self,
        externalBinding: SoftLayer_User_External_Binding
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeExternalBinding',
            externalBinding
        )
        
        return data


    def removeHardwareAccess(
        self,
        hardwareId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeHardwareAccess',
            hardwareId
        )
        
        return data


    def removePortalPermission(
        self,
        permission: SoftLayer_User_Customer_CustomerPermission_Permission,
        cascadePermissionsFlag: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removePortalPermission',
            permission,
            cascadePermissionsFlag
        )
        
        return data


    def removeRole(
        self,
        role: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeRole',
            role
        )
        
        return data


    def removeSecurityAnswers(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeSecurityAnswers',
            
        )
        
        return data


    def removeVirtualGuestAccess(
        self,
        virtualGuestId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeVirtualGuestAccess',
            virtualGuestId
        )
        
        return data


    def resetOpenIdConnectLink(
        self,
        providerType: str,
        newIbmIdUsername: str,
        removeSecuritySettings: boolean
    ) -> 'void':

        data = self.client.call(
            self.service,
            'resetOpenIdConnectLink',
            providerType,
            newIbmIdUsername,
            removeSecuritySettings
        )
        
        return data


    def resetOpenIdConnectLinkUnifiedUserManagementMode(
        self,
        providerType: str,
        newIbmIdUsername: str,
        removeSecuritySettings: boolean
    ) -> 'void':

        data = self.client.call(
            self.service,
            'resetOpenIdConnectLinkUnifiedUserManagementMode',
            providerType,
            newIbmIdUsername,
            removeSecuritySettings
        )
        
        return data


    def samlAuthenticate(
        self,
        accountId: str,
        samlResponse: str
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'samlAuthenticate',
            accountId,
            samlResponse
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def samlBeginAuthentication(
        self,
        accountId: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'samlBeginAuthentication',
            accountId
        )
        
        return data


    def samlBeginLogout(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'samlBeginLogout',
            
        )
        
        return data


    def samlLogout(
        self,
        samlResponse: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'samlLogout',
            samlResponse
        )
        
        return data


    def silentlyMigrateUserOpenIdConnect(
        self,
        providerType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'silentlyMigrateUserOpenIdConnect',
            providerType
        )
        
        return data


    def updateNotificationSubscriber(
        self,
        notificationKeyName: str,
        active: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateNotificationSubscriber',
            notificationKeyName,
            active
        )
        
        return data


    def updateSecurityAnswers(
        self,
        questions: SoftLayer_User_Security_Question,
        answers: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateSecurityAnswers',
            questions,
            answers
        )
        
        return data


    def updateSubscriberDeliveryMethod(
        self,
        notificationKeyName: str,
        deliveryMethodKeyNames: str,
        active: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateSubscriberDeliveryMethod',
            notificationKeyName,
            deliveryMethodKeyNames,
            active
        )
        
        return data


    def updateVpnPassword(
        self,
        password: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateVpnPassword',
            password
        )
        
        return data


    def validateAuthenticationToken(
        self,
        authenticationToken: SoftLayer_Container_User_Authentication_Token
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'validateAuthenticationToken',
            authenticationToken
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getActions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Action]':

        data = self.client.call(
            self.service,
            'getActions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Action import Action
        return Action(data)


    def getAdditionalEmails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_AdditionalEmail]':

        data = self.client.call(
            self.service,
            'getAdditionalEmails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.AdditionalEmail import AdditionalEmail
        return AdditionalEmail(data)


    def getApiAuthenticationKeys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_ApiAuthentication]':

        data = self.client.call(
            self.service,
            'getApiAuthenticationKeys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return ApiAuthentication(data)


    def getChildUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getChildUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getClosedTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getClosedTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getDedicatedHosts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_DedicatedHost]':

        data = self.client.call(
            self.service,
            'getDedicatedHosts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getExternalBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_External_Binding]':

        data = self.client.call(
            self.service,
            'getExternalBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.External.Binding import Binding
        return Binding(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareNotifications(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareNotifications',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def getHasAcknowledgedSupportPolicyFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasAcknowledgedSupportPolicyFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullDedicatedHostAccessFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullDedicatedHostAccessFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullHardwareAccessFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullHardwareAccessFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullVirtualGuestAccessFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullVirtualGuestAccessFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIbmIdLink(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Link':

        data = self.client.call(
            self.service,
            'getIbmIdLink',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Link import Link
        return Link(data)


    def getLayoutProfiles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'getLayoutProfiles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def getLocale(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale':

        data = self.client.call(
            self.service,
            'getLocale',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


    def getLoginAttempts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getLoginAttempts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getMobileDevices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_MobileDevice]':

        data = self.client.call(
            self.service,
            'getMobileDevices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice import MobileDevice
        return MobileDevice(data)


    def getNotificationSubscribers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Subscriber]':

        data = self.client.call(
            self.service,
            'getNotificationSubscribers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Subscriber import Subscriber
        return Subscriber(data)


    def getOpenTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOverrides(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Service_Vpn_Overrides]':

        data = self.client.call(
            self.service,
            'getOverrides',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Service.Vpn.Overrides import Overrides
        return Overrides(data)


    def getParent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getParent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getPermissions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_CustomerPermission_Permission]':

        data = self.client.call(
            self.service,
            'getPermissions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.CustomerPermission.Permission import Permission
        return Permission(data)


    def getPreferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Preference]':

        data = self.client.call(
            self.service,
            'getPreferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def getRoles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Role]':

        data = self.client.call(
            self.service,
            'getRoles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getSecurityAnswers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Security_Answer]':

        data = self.client.call(
            self.service,
            'getSecurityAnswers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Security.Answer import Answer
        return Answer(data)


    def getSubscribers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getSubscribers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getSuccessfulLogins(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getSuccessfulLogins',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getSupportPolicyAcknowledgementRequiredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getSupportPolicyAcknowledgementRequiredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSurveyRequiredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getSurveyRequiredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSurveys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Survey]':

        data = self.client.call(
            self.service,
            'getSurveys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Survey import Survey
        return Survey(data)


    def getTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTimezone(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale_Timezone':

        data = self.client.call(
            self.service,
            'getTimezone',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale.Timezone import Timezone
        return Timezone(data)


    def getUnsuccessfulLogins(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getUnsuccessfulLogins',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getUserLinks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Link]':

        data = self.client.call(
            self.service,
            'getUserLinks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Link import Link
        return Link(data)


    def getUserStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Status':

        data = self.client.call(
            self.service,
            'getUserStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Status import Status
        return Status(data)


    def getVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


