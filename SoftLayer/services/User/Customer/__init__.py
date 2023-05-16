# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer'
        self.client = client

    def acknowledgeSupportPolicy(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'acknowledgeSupportPolicy',
            id=identifier
        )
        
        return data


    def addApiAuthenticationKey(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'addApiAuthenticationKey',
            id=identifier
        )
        
        return data


    def addBulkDedicatedHostAccess(
        self,
        dedicatedHostIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkDedicatedHostAccess',
            dedicatedHostIds,
            id=identifier
        )
        
        return data


    def addBulkHardwareAccess(
        self,
        hardwareIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkHardwareAccess',
            hardwareIds,
            id=identifier
        )
        
        return data


    def addBulkPortalPermission(
        self,
        permissions: 'SoftLayer_User_Customer_CustomerPermission_Permission',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkPortalPermission',
            permissions,
            id=identifier
        )
        
        return data


    def addBulkRoles(
        self,
        roles: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addBulkRoles',
            roles,
            id=identifier
        )
        
        return data


    def addBulkVirtualGuestAccess(
        self,
        virtualGuestIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkVirtualGuestAccess',
            virtualGuestIds,
            id=identifier
        )
        
        return data


    def addDedicatedHostAccess(
        self,
        dedicatedHostId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addDedicatedHostAccess',
            dedicatedHostId,
            id=identifier
        )
        
        return data


    def addExternalBinding(
        self,
        externalBinding: 'SoftLayer_User_External_Binding',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_External_Binding':

        data = self.client.call(
            self.service,
            'addExternalBinding',
            externalBinding,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.External.Binding import Binding
        return Binding(data)


    def addHardwareAccess(
        self,
        hardwareId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addHardwareAccess',
            hardwareId,
            id=identifier
        )
        
        return data


    def addNotificationSubscriber(
        self,
        notificationKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addNotificationSubscriber',
            notificationKeyName,
            id=identifier
        )
        
        return data


    def addPortalPermission(
        self,
        permission: 'SoftLayer_User_Customer_CustomerPermission_Permission',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addPortalPermission',
            permission,
            id=identifier
        )
        
        return data


    def addRole(
        self,
        role: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addRole',
            role,
            id=identifier
        )
        
        return data


    def addVirtualGuestAccess(
        self,
        virtualGuestId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addVirtualGuestAccess',
            virtualGuestId,
            id=identifier
        )
        
        return data


    def assignNewParentId(
        self,
        parentId: int,
        cascadePermissionsFlag: bool,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'assignNewParentId',
            parentId,
            cascadePermissionsFlag,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def changePreference(
        self,
        preferenceTypeKeyName: str,
        value: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Preference]':

        data = self.client.call(
            self.service,
            'changePreference',
            preferenceTypeKeyName,
            value,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def createNotificationSubscriber(
        self,
        keyName: str,
        resourceTableId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createNotificationSubscriber',
            keyName,
            resourceTableId,
            id=identifier
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_User_Customer',
        password: str,
        vpnPassword: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            password,
            vpnPassword,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def createSubscriberDeliveryMethods(
        self,
        notificationKeyName: str,
        deliveryMethodKeyNames: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createSubscriberDeliveryMethods',
            notificationKeyName,
            deliveryMethodKeyNames,
            id=identifier
        )
        
        return data


    def deactivateNotificationSubscriber(
        self,
        keyName: str,
        resourceTableId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deactivateNotificationSubscriber',
            keyName,
            resourceTableId,
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_User_Customer',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def editObjects(
        self,
        templateObjects: 'SoftLayer_User_Customer'
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
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'findUserPreference',
            profileName,
            containerKeyname,
            preferenceKeyname,
            id=identifier,
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
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAgentImpersonationToken',
            id=identifier
        )
        
        return data


    def getAllowedDedicatedHostIds(
        self,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedDedicatedHostIds',
            id=identifier
        )
        
        return data


    def getAllowedHardwareIds(
        self,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedHardwareIds',
            id=identifier
        )
        
        return data


    def getAllowedVirtualGuestIds(
        self,
        identifier: int
    ) -> 'list[int]':

        data = self.client.call(
            self.service,
            'getAllowedVirtualGuestIds',
            id=identifier
        )
        
        return data


    def getAuthenticationToken(
        self,
        token: 'SoftLayer_Container_User_Authentication_Token',
        identifier: int
    ) -> 'SoftLayer_Container_User_Authentication_Token':

        data = self.client.call(
            self.service,
            'getAuthenticationToken',
            token,
            id=identifier
        )
        from SoftLayer.datatypes.Container.User.Authentication.Token import Token
        return Token(data)


    def getDefaultAccount(
        self,
        providerType: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getDefaultAccount',
            providerType,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getHardwareCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getHardwareCount',
            id=identifier
        )
        
        return data


    def getImpersonationToken(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getImpersonationToken',
            id=identifier
        )
        
        return data


    def getLoginToken(
        self,
        request: 'SoftLayer_Container_Authentication_Request_Contract'
    ) -> 'SoftLayer_Container_Authentication_Response_Common':

        data = self.client.call(
            self.service,
            'getLoginToken',
            request
        )
        from SoftLayer.datatypes.Container.Authentication.Response.Common import Common
        return Common(data)


    def getMappedAccounts(
        self,
        providerType: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account]':

        data = self.client.call(
            self.service,
            'getMappedAccounts',
            providerType,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getOpenIdConnectMigrationState(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_User_Customer_OpenIdConnect_MigrationState':

        data = self.client.call(
            self.service,
            'getOpenIdConnectMigrationState',
            id=identifier
        )
        from SoftLayer.datatypes.Container.User.Customer.OpenIdConnect.MigrationState import MigrationState
        return MigrationState(data)


    def getPasswordRequirements(
        self,
        isVpn: bool
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
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Preference':

        data = self.client.call(
            self.service,
            'getPreference',
            preferenceTypeKeyName,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def getPreferenceTypes(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Preference_Type]':

        data = self.client.call(
            self.service,
            'getPreferenceTypes',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Preference.Type import Type
        return Type(data)


    def getRequirementsForPasswordSet(
        self,
        passwordSet: 'SoftLayer_Container_User_Customer_PasswordSet',
        identifier: int
    ) -> 'SoftLayer_Container_User_Customer_PasswordSet':

        data = self.client.call(
            self.service,
            'getRequirementsForPasswordSet',
            passwordSet,
            id=identifier
        )
        from SoftLayer.datatypes.Container.User.Customer.PasswordSet import PasswordSet
        return PasswordSet(data)


    def getSupportPolicyDocument(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getSupportPolicyDocument',
            id=identifier
        )
        
        return data


    def getSupportPolicyName(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportPolicyName',
            id=identifier
        )
        
        return data


    def getSupportedLocales(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Locale]':

        data = self.client.call(
            self.service,
            'getSupportedLocales',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


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


    def getUserPreferences(
        self,
        profileName: str,
        containerKeyname: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'getUserPreferences',
            profileName,
            containerKeyname,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def getVirtualGuestCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getVirtualGuestCount',
            id=identifier
        )
        
        return data


    def inTerminalStatus(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'inTerminalStatus',
            id=identifier
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
        username: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'initiatePortalPasswordChangeByBrandAgent',
            username,
            id=identifier
        )
        
        return data


    def inviteUserToLinkOpenIdConnect(
        self,
        providerType: str,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'inviteUserToLinkOpenIdConnect',
            providerType,
            id=identifier
        )
        
        return data


    def isMasterUser(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isMasterUser',
            id=identifier
        )
        
        return data


    def isValidPortalPassword(
        self,
        password: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isValidPortalPassword',
            password,
            id=identifier
        )
        
        return data


    def performExternalAuthentication(
        self,
        authenticationContainer: 'SoftLayer_Container_User_Customer_External_Binding'
    ) -> 'SoftLayer_Container_User_Customer_Portal_Token':

        data = self.client.call(
            self.service,
            'performExternalAuthentication',
            authenticationContainer
        )
        from SoftLayer.datatypes.Container.User.Customer.Portal.Token import Token
        return Token(data)


    def processPasswordSetRequest(
        self,
        passwordSet: 'SoftLayer_Container_User_Customer_PasswordSet',
        authenticationContainer: 'SoftLayer_Container_User_Customer_External_Binding',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'processPasswordSetRequest',
            passwordSet,
            authenticationContainer,
            id=identifier
        )
        
        return data


    def removeAllDedicatedHostAccessForThisUser(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllDedicatedHostAccessForThisUser',
            id=identifier
        )
        
        return data


    def removeAllHardwareAccessForThisUser(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllHardwareAccessForThisUser',
            id=identifier
        )
        
        return data


    def removeAllVirtualAccessForThisUser(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllVirtualAccessForThisUser',
            id=identifier
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
        dedicatedHostIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkDedicatedHostAccess',
            dedicatedHostIds,
            id=identifier
        )
        
        return data


    def removeBulkHardwareAccess(
        self,
        hardwareIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkHardwareAccess',
            hardwareIds,
            id=identifier
        )
        
        return data


    def removeBulkPortalPermission(
        self,
        permissions: 'SoftLayer_User_Customer_CustomerPermission_Permission',
        cascadePermissionsFlag: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkPortalPermission',
            permissions,
            cascadePermissionsFlag,
            id=identifier
        )
        
        return data


    def removeBulkRoles(
        self,
        roles: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeBulkRoles',
            roles,
            id=identifier
        )
        
        return data


    def removeBulkVirtualGuestAccess(
        self,
        virtualGuestIds: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkVirtualGuestAccess',
            virtualGuestIds,
            id=identifier
        )
        
        return data


    def removeDedicatedHostAccess(
        self,
        dedicatedHostId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeDedicatedHostAccess',
            dedicatedHostId,
            id=identifier
        )
        
        return data


    def removeExternalBinding(
        self,
        externalBinding: 'SoftLayer_User_External_Binding',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeExternalBinding',
            externalBinding,
            id=identifier
        )
        
        return data


    def removeHardwareAccess(
        self,
        hardwareId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeHardwareAccess',
            hardwareId,
            id=identifier
        )
        
        return data


    def removePortalPermission(
        self,
        permission: 'SoftLayer_User_Customer_CustomerPermission_Permission',
        cascadePermissionsFlag: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removePortalPermission',
            permission,
            cascadePermissionsFlag,
            id=identifier
        )
        
        return data


    def removeRole(
        self,
        role: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeRole',
            role,
            id=identifier
        )
        
        return data


    def removeSecurityAnswers(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeSecurityAnswers',
            id=identifier
        )
        
        return data


    def removeVirtualGuestAccess(
        self,
        virtualGuestId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeVirtualGuestAccess',
            virtualGuestId,
            id=identifier
        )
        
        return data


    def resetOpenIdConnectLink(
        self,
        providerType: str,
        newIbmIdUsername: str,
        removeSecuritySettings: bool,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'resetOpenIdConnectLink',
            providerType,
            newIbmIdUsername,
            removeSecuritySettings,
            id=identifier
        )
        
        return data


    def resetOpenIdConnectLinkUnifiedUserManagementMode(
        self,
        providerType: str,
        newIbmIdUsername: str,
        removeSecuritySettings: bool,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'resetOpenIdConnectLinkUnifiedUserManagementMode',
            providerType,
            newIbmIdUsername,
            removeSecuritySettings,
            id=identifier
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
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'samlBeginLogout',
            id=identifier
        )
        
        return data


    def samlLogout(
        self,
        samlResponse: str,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'samlLogout',
            samlResponse,
            id=identifier
        )
        
        return data


    def selfPasswordChange(
        self,
        currentPassword: str,
        newPassword: str,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'selfPasswordChange',
            currentPassword,
            newPassword,
            id=identifier
        )
        
        return data


    def setDefaultAccount(
        self,
        providerType: str,
        accountId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'setDefaultAccount',
            providerType,
            accountId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def silentlyMigrateUserOpenIdConnect(
        self,
        providerType: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'silentlyMigrateUserOpenIdConnect',
            providerType,
            id=identifier
        )
        
        return data


    def turnOffMasterUserPermissionCheckMode(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'turnOffMasterUserPermissionCheckMode',
            id=identifier
        )
        
        return data


    def turnOnMasterUserPermissionCheckMode(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'turnOnMasterUserPermissionCheckMode',
            id=identifier
        )
        
        return data


    def updateNotificationSubscriber(
        self,
        notificationKeyName: str,
        active: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateNotificationSubscriber',
            notificationKeyName,
            active,
            id=identifier
        )
        
        return data


    def updateSecurityAnswers(
        self,
        questions: 'SoftLayer_User_Security_Question',
        answers: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateSecurityAnswers',
            questions,
            answers,
            id=identifier
        )
        
        return data


    def updateSubscriberDeliveryMethod(
        self,
        notificationKeyName: str,
        deliveryMethodKeyNames: str,
        active: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateSubscriberDeliveryMethod',
            notificationKeyName,
            deliveryMethodKeyNames,
            active,
            id=identifier
        )
        
        return data


    def updateVpnPassword(
        self,
        password: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateVpnPassword',
            password,
            id=identifier
        )
        
        return data


    def updateVpnUser(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateVpnUser',
            id=identifier
        )
        
        return data


    def validateAuthenticationToken(
        self,
        authenticationToken: 'SoftLayer_Container_User_Authentication_Token'
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
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getActions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Action]':

        data = self.client.call(
            self.service,
            'getActions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Action import Action
        return Action(data)


    def getAdditionalEmails(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_AdditionalEmail]':

        data = self.client.call(
            self.service,
            'getAdditionalEmails',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.AdditionalEmail import AdditionalEmail
        return AdditionalEmail(data)


    def getApiAuthenticationKeys(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_ApiAuthentication]':

        data = self.client.call(
            self.service,
            'getApiAuthenticationKeys',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.ApiAuthentication import ApiAuthentication
        return ApiAuthentication(data)


    def getChildUsers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getChildUsers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getClosedTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getClosedTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getDedicatedHosts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_DedicatedHost]':

        data = self.client.call(
            self.service,
            'getDedicatedHosts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getExternalBindings(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_External_Binding]':

        data = self.client.call(
            self.service,
            'getExternalBindings',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.External.Binding import Binding
        return Binding(data)


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareNotifications(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareNotifications',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def getHasAcknowledgedSupportPolicyFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasAcknowledgedSupportPolicyFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullDedicatedHostAccessFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullDedicatedHostAccessFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullHardwareAccessFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullHardwareAccessFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasFullVirtualGuestAccessFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasFullVirtualGuestAccessFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIbmIdLink(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Link':

        data = self.client.call(
            self.service,
            'getIbmIdLink',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Link import Link
        return Link(data)


    def getLayoutProfiles(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Profile]':

        data = self.client.call(
            self.service,
            'getLayoutProfiles',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def getLocale(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale':

        data = self.client.call(
            self.service,
            'getLocale',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


    def getLoginAttempts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getLoginAttempts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getMobileDevices(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_MobileDevice]':

        data = self.client.call(
            self.service,
            'getMobileDevices',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice import MobileDevice
        return MobileDevice(data)


    def getNotificationSubscribers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Subscriber]':

        data = self.client.call(
            self.service,
            'getNotificationSubscribers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Subscriber import Subscriber
        return Subscriber(data)


    def getOpenTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOverrides(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Service_Vpn_Overrides]':

        data = self.client.call(
            self.service,
            'getOverrides',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Service.Vpn.Overrides import Overrides
        return Overrides(data)


    def getParent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getParent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getPermissions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_CustomerPermission_Permission]':

        data = self.client.call(
            self.service,
            'getPermissions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.CustomerPermission.Permission import Permission
        return Permission(data)


    def getPreferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Preference]':

        data = self.client.call(
            self.service,
            'getPreferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Preference import Preference
        return Preference(data)


    def getRoles(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Role]':

        data = self.client.call(
            self.service,
            'getRoles',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getSecurityAnswers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Security_Answer]':

        data = self.client.call(
            self.service,
            'getSecurityAnswers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Security.Answer import Answer
        return Answer(data)


    def getSubscribers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getSubscribers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getSuccessfulLogins(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getSuccessfulLogins',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getSupportPolicyAcknowledgementRequiredFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getSupportPolicyAcknowledgementRequiredFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSurveyRequiredFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getSurveyRequiredFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSurveys(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Survey]':

        data = self.client.call(
            self.service,
            'getSurveys',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Survey import Survey
        return Survey(data)


    def getTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTimezone(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale_Timezone':

        data = self.client.call(
            self.service,
            'getTimezone',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale.Timezone import Timezone
        return Timezone(data)


    def getUnsuccessfulLogins(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Access_Authentication]':

        data = self.client.call(
            self.service,
            'getUnsuccessfulLogins',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Access.Authentication import Authentication
        return Authentication(data)


    def getUserLinks(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_Link]':

        data = self.client.call(
            self.service,
            'getUserLinks',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.Link import Link
        return Link(data)


    def getUserStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Status':

        data = self.client.call(
            self.service,
            'getUserStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Status import Status
        return Status(data)


    def getVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


