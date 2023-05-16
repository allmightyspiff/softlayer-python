# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_OpenIdConnect(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_OpenIdConnect'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_User_Customer_OpenIdConnect,
        password: str,
        vpnPassword: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_OpenIdConnect':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            password,
            vpnPassword,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.OpenIdConnect import OpenIdConnect
        return SL_OpenIdConnect(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_LoginAccountInfo(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_OpenIdConnect':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.OpenIdConnect import OpenIdConnect
        return SL_OpenIdConnect(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_RegistrationInformation(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_PasswordSet(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_OpenIdConnect(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def acknowledgeSupportPolicy(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'acknowledgeSupportPolicy',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addApiAuthenticationKey(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'addApiAuthenticationKey',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Binding(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Profile(data)

# This file was automatically generated with tools/generateTypes.py
    def getActiveExternalAuthenticationVendors(
        self,
        
    ) -> 'list[SoftLayer_Container_User_Customer_External_Binding_Vendor]':
        data = self.client.call(
            self.service,
            'getActiveExternalAuthenticationVendors',
            
        )
        from SoftLayer.datatypes.Container.User.Customer.External.Binding.Vendor import Vendor
        return SL_Vendor(data)

# This file was automatically generated with tools/generateTypes.py
    def getAgentImpersonationToken(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getAgentImpersonationToken',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllowedDedicatedHostIds(
        self,
        
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getAllowedDedicatedHostIds',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllowedHardwareIds(
        self,
        
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getAllowedHardwareIds',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllowedVirtualGuestIds(
        self,
        
    ) -> 'list[int]':
        data = self.client.call(
            self.service,
            'getAllowedVirtualGuestIds',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardwareCount(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getHardwareCount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getImpersonationToken(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getImpersonationToken',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Common(data)

# This file was automatically generated with tools/generateTypes.py
    def getOpenIdConnectMigrationState(
        self,
        
    ) -> 'SoftLayer_Container_User_Customer_OpenIdConnect_MigrationState':
        data = self.client.call(
            self.service,
            'getOpenIdConnectMigrationState',
            
        )
        from SoftLayer.datatypes.Container.User.Customer.OpenIdConnect.MigrationState import MigrationState
        return SL_MigrationState(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_PasswordSet(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getSupportPolicyDocument(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getSupportPolicyDocument',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getSupportPolicyName(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getSupportPolicyName',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Locale(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Profile(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualGuestCount(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getVirtualGuestCount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def inTerminalStatus(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'inTerminalStatus',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def isMasterUser(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isMasterUser',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
    def removeAllDedicatedHostAccessForThisUser(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAllDedicatedHostAccessForThisUser',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAllHardwareAccessForThisUser(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAllHardwareAccessForThisUser',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAllVirtualAccessForThisUser(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAllVirtualAccessForThisUser',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def removeSecurityAnswers(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeSecurityAnswers',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def samlBeginLogout(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'samlBeginLogout',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def turnOffMasterUserPermissionCheckMode(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'turnOffMasterUserPermissionCheckMode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def turnOnMasterUserPermissionCheckMode(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'turnOnMasterUserPermissionCheckMode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def updateVpnUser(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'updateVpnUser',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Token(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Action(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_AdditionalEmail(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ApiAuthentication(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_DedicatedHost(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Binding(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Link(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Profile(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Locale(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Authentication(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_MobileDevice(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Subscriber(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Overrides(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Permission(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Role(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Answer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Subscriber(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Authentication(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Survey(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Timezone(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Authentication(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Link(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Guest(data)


