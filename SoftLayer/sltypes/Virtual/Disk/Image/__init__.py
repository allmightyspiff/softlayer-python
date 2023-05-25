from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Disk_Image(Entity):
    """The virtual disk image data type presents the structure in which a virtual disk image will be presented.
Virtual block devices are assigned to disk images."""
    capacity: int
    checksum: str
    checksumAlgorithm: str
    createDate: datetime
    description: str
    id_: int
    modifyDate: datetime
    name: str
    parentId: int
    storageRepositoryId: int
    typeId: int
    units: str
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Disk_Image'

    def editObject(self, identifier: int, templateObject: 'Virtual_Disk_Image') -> bool:
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'editObject', templateObject, id=identifier)
        return data

    def getAvailableBootModes(self) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getAvailableBootModes')
        return data

    def getObject(self, identifier: int) -> 'Virtual_Disk_Image':
        """Retrieve a SoftLayer_Virtual_Disk_Image record."""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getPublicIsoImages(self) -> list['Virtual_Disk_Image']:
        """Retrieves images from the public ISO repository."""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getPublicIsoImages')
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Virtual_Disk_Image':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Virtual_Disk_Image import Billing_Item_Virtual_Disk_Image
        return data

    def getBlockDevices(self, identifier: int) -> list['Virtual_Guest_Block_Device']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getBlockDevices', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device import Virtual_Guest_Block_Device
        return data

    def getBootableVolumeFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getBootableVolumeFlag', id=identifier)
        return data

    def getCloudInitFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getCloudInitFlag', id=identifier)
        return data

    def getCoalescedDiskImages(self, identifier: int) -> list['Virtual_Disk_Image']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getCoalescedDiskImages', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getCopyOnWriteFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getCopyOnWriteFlag', id=identifier)
        return data

    def getDiskFileExtension(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getDiskFileExtension', id=identifier)
        return data

    def getDiskImageStorageGroup(self, identifier: int) -> 'Configuration_Storage_Group':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getDiskImageStorageGroup', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group import Configuration_Storage_Group
        return data

    def getImportedDiskType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getImportedDiskType', id=identifier)
        return data

    def getIsEncrypted(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getIsEncrypted', id=identifier)
        return data

    def getLocalDiskFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getLocalDiskFlag', id=identifier)
        return data

    def getMetadataFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getMetadataFlag', id=identifier)
        return data

    def getSoftwareReferences(self, identifier: int) -> list['Virtual_Disk_Image_Software']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getSoftwareReferences', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image_Software import Virtual_Disk_Image_Software
        return data

    def getSourceDiskImage(self, identifier: int) -> 'Virtual_Disk_Image':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getSourceDiskImage', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getStorageGroupDetails(self, identifier: int) -> 'Container_Image_StorageGroupDetails':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getStorageGroupDetails', id=identifier)
        from SoftLayer.sltypes.Container_Image_StorageGroupDetails import Container_Image_StorageGroupDetails
        return data

    def getStorageGroups(self, identifier: int) -> list['Configuration_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getStorageGroups', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group import Configuration_Storage_Group
        return data

    def getStorageRepository(self, identifier: int) -> 'Virtual_Storage_Repository':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getStorageRepository', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository import Virtual_Storage_Repository
        return data

    def getStorageRepositoryType(self, identifier: int) -> 'Virtual_Storage_Repository_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getStorageRepositoryType', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository_Type import Virtual_Storage_Repository_Type
        return data

    def getSupportedHardware(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getSupportedHardware', id=identifier)
        return data

    def getTemplateBlockDevice(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getTemplateBlockDevice', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template import Virtual_Guest_Block_Device_Template
        return data

    def getType(self, identifier: int) -> 'Virtual_Disk_Image_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Disk_Image', 'getType', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image_Type import Virtual_Disk_Image_Type
        return data
