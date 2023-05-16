# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest_Block_Device_Template_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest_Block_Device_Template_Group'
        self.client = client

    def addByolAttribute(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addByolAttribute',
            id=identifier
        )
        
        return data


    def addCloudInitAttribute(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addCloudInitAttribute',
            id=identifier
        )
        
        return data


    def addLocations(
        self,
        locations: 'SoftLayer_Location',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addLocations',
            locations,
            id=identifier
        )
        
        return data


    def addSupportedBootMode(
        self,
        bootMode: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addSupportedBootMode',
            bootMode,
            id=identifier
        )
        
        return data


    def copyToExternalSource(
        self,
        configuration: 'SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'copyToExternalSource',
            configuration,
            id=identifier
        )
        
        return data


    def copyToIcos(
        self,
        configuration: 'SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'copyToIcos',
            configuration,
            id=identifier
        )
        
        return data


    def createFromExternalSource(
        self,
        configuration: 'SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'createFromExternalSource',
            configuration,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def createFromIcos(
        self,
        configuration: 'SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'createFromIcos',
            configuration,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def createPublicArchiveTransaction(
        self,
        groupName: str,
        summary: str,
        note: str,
        locations: 'SoftLayer_Location',
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'createPublicArchiveTransaction',
            groupName,
            summary,
            note,
            locations,
            id=identifier
        )
        
        return data


    def deleteByolAttribute(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteByolAttribute',
            id=identifier
        )
        
        return data


    def deleteCloudInitAttribute(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteCloudInitAttribute',
            id=identifier
        )
        
        return data


    def deleteObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def denySharingAccess(
        self,
        accountId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'denySharingAccess',
            accountId,
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Virtual_Guest_Block_Device_Template_Group',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def findGcImagesByCurrentUser(
        self,
        dataCenters: str,
        regions: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'findGcImagesByCurrentUser',
            dataCenters,
            regions,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getAllAvailableCompatiblePlatformNames(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAllAvailableCompatiblePlatformNames',
            
        )
        
        return data


    def getBootMode(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBootMode',
            id=identifier
        )
        
        return data


    def getCurrentCompatiblePlatformNames(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getCurrentCompatiblePlatformNames',
            id=identifier
        )
        
        return data


    def getDefaultBootMode(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDefaultBootMode',
            id=identifier
        )
        
        return data


    def getEncryptionAttributes(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getEncryptionAttributes',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getPublicCustomerOwnedImages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getPublicCustomerOwnedImages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getPublicImages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getPublicImages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getRiasAccount(
        self,
        secret: str
    ) -> 'SoftLayer_Container_Virtual_Guest_Block_Device_Template_Group_RiasAccount':

        data = self.client.call(
            self.service,
            'getRiasAccount',
            secret
        )
        from SoftLayer.datatypes.Container.Virtual.Guest.Block.Device.Template.Group.RiasAccount import RiasAccount
        return RiasAccount(data)


    def getStorageLocations(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getStorageLocations',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getSupportedBootModes(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getSupportedBootModes',
            id=identifier
        )
        
        return data


    def getTemplateDataCenterName(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTemplateDataCenterName',
            id=identifier
        )
        
        return data


    def getVhdImportSoftwareDescriptions(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Software_Description]':

        data = self.client.call(
            self.service,
            'getVhdImportSoftwareDescriptions',
            mask=objectMask
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def isByol(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isByol',
            id=identifier
        )
        
        return data


    def isByolCapableOperatingSystem(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isByolCapableOperatingSystem',
            id=identifier
        )
        
        return data


    def isByolOnlyOperatingSystem(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isByolOnlyOperatingSystem',
            id=identifier
        )
        
        return data


    def isCloudInit(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isCloudInit',
            id=identifier
        )
        
        return data


    def isCloudInitOnlyOperatingSystem(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isCloudInitOnlyOperatingSystem',
            id=identifier
        )
        
        return data


    def isEncrypted(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isEncrypted',
            id=identifier
        )
        
        return data


    def permitSharingAccess(
        self,
        accountId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'permitSharingAccess',
            accountId,
            id=identifier
        )
        
        return data


    def removeCompatiblePlatforms(
        self,
        platformNames: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeCompatiblePlatforms',
            platformNames,
            id=identifier
        )
        
        return data


    def removeLocations(
        self,
        locations: 'SoftLayer_Location',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeLocations',
            locations,
            id=identifier
        )
        
        return data


    def removeSupportedBootMode(
        self,
        bootMode: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeSupportedBootMode',
            bootMode,
            id=identifier
        )
        
        return data


    def setAvailableLocations(
        self,
        locations: 'SoftLayer_Location',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setAvailableLocations',
            locations,
            id=identifier
        )
        
        return data


    def setBootMode(
        self,
        newBootMode: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setBootMode',
            newBootMode,
            id=identifier
        )
        
        return data


    def setCompatiblePlatforms(
        self,
        platformNames: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setCompatiblePlatforms',
            platformNames,
            id=identifier
        )
        
        return data


    def setTags(
        self,
        tags: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setTags',
            tags,
            id=identifier
        )
        
        return data


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


    def getAccountContacts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Contact]':

        data = self.client.call(
            self.service,
            'getAccountContacts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


    def getAccountReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts]':

        data = self.client.call(
            self.service,
            'getAccountReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group.Accounts import Accounts
        return Accounts(data)


    def getBlockDevices(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template]':

        data = self.client.call(
            self.service,
            'getBlockDevices',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template import Template
        return Template(data)


    def getBlockDevicesDiskSpaceTotal(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getBlockDevicesDiskSpaceTotal',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getByolFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getByolFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getChildren(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getChildren',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getDatacenter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDatacenters(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getDatacenters',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getFirstChild(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'getFirstChild',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getFlexImageFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getFlexImageFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGlobalIdentifier(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getImageType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Disk_Image_Type':

        data = self.client.call(
            self.service,
            'getImageType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Disk.Image.Type import Type
        return Type(data)


    def getImageTypeKeyName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getImageTypeKeyName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextGenFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNextGenFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getParent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':

        data = self.client.call(
            self.service,
            'getParent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getRegion(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getRegion',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getRegions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Service_Resource]':

        data = self.client.call(
            self.service,
            'getRegions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getSshKeys(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':

        data = self.client.call(
            self.service,
            'getSshKeys',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return Key(data)


    def getStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group.Status import Status
        return Status(data)


    def getStorageRepository(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository':

        data = self.client.call(
            self.service,
            'getStorageRepository',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getTagReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':

        data = self.client.call(
            self.service,
            'getTagReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return Reference(data)


    def getTransaction(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':

        data = self.client.call(
            self.service,
            'getTransaction',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


