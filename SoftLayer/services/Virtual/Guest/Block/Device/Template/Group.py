# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest_Block_Device_Template_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest_Block_Device_Template_Group'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addByolAttribute(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addByolAttribute',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addCloudInitAttribute(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addCloudInitAttribute',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addLocations(
        self,
        locations: SoftLayer_Location
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addLocations',
            locations
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addSupportedBootMode(
        self,
        bootMode: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addSupportedBootMode',
            bootMode
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def copyToExternalSource(
        self,
        configuration: SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'copyToExternalSource',
            configuration
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def copyToIcos(
        self,
        configuration: SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'copyToIcos',
            configuration
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createFromExternalSource(
        self,
        configuration: SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':
        data = self.client.call(
            self.service,
            'createFromExternalSource',
            configuration,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def createFromIcos(
        self,
        configuration: SoftLayer_Container_Virtual_Guest_Block_Device_Template_Configuration,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':
        data = self.client.call(
            self.service,
            'createFromIcos',
            configuration,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def createPublicArchiveTransaction(
        self,
        groupName: str,
        summary: str,
        note: str,
        locations: SoftLayer_Location
    ) -> 'int':
        data = self.client.call(
            self.service,
            'createPublicArchiveTransaction',
            groupName,
            summary,
            note,
            locations
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteByolAttribute(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteByolAttribute',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteCloudInitAttribute(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteCloudInitAttribute',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':
        data = self.client.call(
            self.service,
            'deleteObject',
            mask=objectMask
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def denySharingAccess(
        self,
        accountId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'denySharingAccess',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Virtual_Guest_Block_Device_Template_Group
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllAvailableCompatiblePlatformNames(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAllAvailableCompatiblePlatformNames',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBootMode(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getBootMode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCurrentCompatiblePlatformNames(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getCurrentCompatiblePlatformNames',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDefaultBootMode(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDefaultBootMode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getEncryptionAttributes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getEncryptionAttributes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_RiasAccount(data)

# This file was automatically generated with tools/generateTypes.py
    def getStorageLocations(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':
        data = self.client.call(
            self.service,
            'getStorageLocations',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getSupportedBootModes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getSupportedBootModes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getTemplateDataCenterName(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getTemplateDataCenterName',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Description(data)

# This file was automatically generated with tools/generateTypes.py
    def isByol(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isByol',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isByolCapableOperatingSystem(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isByolCapableOperatingSystem',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isByolOnlyOperatingSystem(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isByolOnlyOperatingSystem',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isCloudInit(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isCloudInit',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isCloudInitOnlyOperatingSystem(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isCloudInitOnlyOperatingSystem',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isEncrypted(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isEncrypted',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def permitSharingAccess(
        self,
        accountId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'permitSharingAccess',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeCompatiblePlatforms(
        self,
        platformNames: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeCompatiblePlatforms',
            platformNames
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeLocations(
        self,
        locations: SoftLayer_Location
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeLocations',
            locations
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeSupportedBootMode(
        self,
        bootMode: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeSupportedBootMode',
            bootMode
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setAvailableLocations(
        self,
        locations: SoftLayer_Location
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setAvailableLocations',
            locations
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setBootMode(
        self,
        newBootMode: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setBootMode',
            newBootMode
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setCompatiblePlatforms(
        self,
        platformNames: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setCompatiblePlatforms',
            platformNames
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setTags(
        self,
        tags: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setTags',
            tags
        )
        
        return data

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
    def getAccountContacts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Contact]':
        data = self.client.call(
            self.service,
            'getAccountContacts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return SL_Contact(data)

# This file was automatically generated with tools/generateTypes.py
    def getAccountReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts]':
        data = self.client.call(
            self.service,
            'getAccountReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group.Accounts import Accounts
        return SL_Accounts(data)

# This file was automatically generated with tools/generateTypes.py
    def getBlockDevices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template]':
        data = self.client.call(
            self.service,
            'getBlockDevices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template import Template
        return SL_Template(data)

# This file was automatically generated with tools/generateTypes.py
    def getBlockDevicesDiskSpaceTotal(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':
        data = self.client.call(
            self.service,
            'getBlockDevicesDiskSpaceTotal',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getByolFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getByolFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getChildren(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':
        data = self.client.call(
            self.service,
            'getChildren',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getDatacenter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getDatacenters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location]':
        data = self.client.call(
            self.service,
            'getDatacenters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirstChild(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':
        data = self.client.call(
            self.service,
            'getFirstChild',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getFlexImageFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getFlexImageFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getGlobalIdentifier(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getGlobalIdentifier',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getImageType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Disk_Image_Type':
        data = self.client.call(
            self.service,
            'getImageType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Disk.Image.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getImageTypeKeyName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getImageTypeKeyName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNextGenFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getNextGenFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getParent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group':
        data = self.client.call(
            self.service,
            'getParent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegion(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Resource':
        data = self.client.call(
            self.service,
            'getRegion',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return SL_Resource(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Service_Resource]':
        data = self.client.call(
            self.service,
            'getRegions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return SL_Resource(data)

# This file was automatically generated with tools/generateTypes.py
    def getSshKeys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':
        data = self.client.call(
            self.service,
            'getSshKeys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return SL_Key(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getStorageRepository(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository':
        data = self.client.call(
            self.service,
            'getStorageRepository',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return SL_Repository(data)

# This file was automatically generated with tools/generateTypes.py
    def getTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':
        data = self.client.call(
            self.service,
            'getTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return SL_Reference(data)

# This file was automatically generated with tools/generateTypes.py
    def getTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction':
        data = self.client.call(
            self.service,
            'getTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return SL_Transaction(data)


