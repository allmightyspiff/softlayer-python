# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Disk_Image(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Disk_Image'
        self.client = client

    def editObject(
        self,
        templateObject: SoftLayer_Virtual_Disk_Image
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAvailableBootModes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAvailableBootModes',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Disk_Image':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getPublicIsoImages(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getPublicIsoImages',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Virtual_Disk_Image':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Virtual.Disk.Image import Image
        return Image(data)


    def getBlockDevices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device]':

        data = self.client.call(
            self.service,
            'getBlockDevices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device import Device
        return Device(data)


    def getBootableVolumeFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBootableVolumeFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCloudInitFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCloudInitFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCoalescedDiskImages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getCoalescedDiskImages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getCopyOnWriteFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCopyOnWriteFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDiskFileExtension(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDiskFileExtension',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDiskImageStorageGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Storage_Group':

        data = self.client.call(
            self.service,
            'getDiskImageStorageGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Storage.Group import Group
        return Group(data)


    def getImportedDiskType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getImportedDiskType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsEncrypted(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsEncrypted',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLocalDiskFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getLocalDiskFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMetadataFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMetadataFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSoftwareReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image_Software]':

        data = self.client.call(
            self.service,
            'getSoftwareReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image.Software import Software
        return Software(data)


    def getSourceDiskImage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Disk_Image':

        data = self.client.call(
            self.service,
            'getSourceDiskImage',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getStorageGroupDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Container_Image_StorageGroupDetails':

        data = self.client.call(
            self.service,
            'getStorageGroupDetails',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Image.StorageGroupDetails import StorageGroupDetails
        return StorageGroupDetails(data)


    def getStorageGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group]':

        data = self.client.call(
            self.service,
            'getStorageGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Group import Group
        return Group(data)


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
        return Repository(data)


    def getStorageRepositoryType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Storage_Repository_Type':

        data = self.client.call(
            self.service,
            'getStorageRepositoryType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository.Type import Type
        return Type(data)


    def getSupportedHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportedHardware',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTemplateBlockDevice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Block_Device_Template':

        data = self.client.call(
            self.service,
            'getTemplateBlockDevice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template import Template
        return Template(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Disk_Image_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Disk.Image.Type import Type
        return Type(data)


