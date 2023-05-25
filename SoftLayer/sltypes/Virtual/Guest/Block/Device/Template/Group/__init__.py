from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_Guest_Block_Device_Template_Group(Entity):
    """The virtual block device template group data type presents the structure in which a group of archived image
templates will be presented. The structure consists of a parent template group which contain multiple child
template group objects.  Each child template group object represents the image template in a particular
location. Unless editing/deleting a specific child template group object, it is best to use the parent
object.   A virtual block device template group, also known as an image template group, represents an image
of a virtual guest instance."""
    accountId: int
    createDate: datetime
    id_: int
    name: str
    note: str
    parentId: int
    publicFlag: int
    statusId: int
    summary: str
    transactionId: int
    userRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_Guest_Block_Device_Template_Group'

    def addByolAttribute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'addByolAttribute', id=identifier)
        return data

    def addCloudInitAttribute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'addCloudInitAttribute', id=identifier)
        return data

    def addLocations(self, identifier: int, locations: 'Location') -> bool:
        """[[SoftLayer_Virtual_Guest_Block_Device]] can be made available in all storage locations. This method will
create transaction(s) to add available locations to an archive image template."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'addLocations', locations, id=identifier)
        return data

    def addSupportedBootMode(self, identifier: int, bootMode: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'addSupportedBootMode', bootMode, id=identifier)
        return data

    def copyToExternalSource(self, identifier: int, configuration: 'Container_Virtual_Guest_Block_Device_Template_Configuration') -> bool:
        """This method generates a transaction to export/copy a template to an external source."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'copyToExternalSource', configuration, id=identifier)
        return data

    def copyToIcos(self, identifier: int, configuration: 'Container_Virtual_Guest_Block_Device_Template_Configuration') -> bool:
        """This method generates a transaction to export/copy a template to IBM Cloud Object Storage (ICOS)"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'copyToIcos', configuration, id=identifier)
        return data

    def createFromExternalSource(self, configuration: 'Container_Virtual_Guest_Block_Device_Template_Configuration') -> 'Virtual_Guest_Block_Device_Template_Group':
        """This method generates a transaction to import a disk image from an external source and create a standard
image template."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'createFromExternalSource', configuration)
        return data

    def createFromIcos(self, configuration: 'Container_Virtual_Guest_Block_Device_Template_Configuration') -> 'Virtual_Guest_Block_Device_Template_Group':
        """This method generates a process instance to import a disk image from ICOS and create a standard image
template."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'createFromIcos', configuration)
        return data

    def createPublicArchiveTransaction(self, identifier: int, groupName: str, summary: str, note: str, locations: 'Location') -> int:
        """[[SoftLayer_Virtual_Guest_Block_Device]] can be published together in a public repository for use by
everyone. This method generates a transaction to perform a public image of the provided archived block
devices."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'createPublicArchiveTransaction', groupName, summary, note, locations, id=identifier)
        return data

    def deleteByolAttribute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'deleteByolAttribute', id=identifier)
        return data

    def deleteCloudInitAttribute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'deleteCloudInitAttribute', id=identifier)
        return data

    def deleteObject(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """Create a transaction that will remove all block device templates from the group and delete the disk images
associated with them."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'deleteObject', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def denySharingAccess(self, identifier: int, accountId: int) -> bool:
        """Deny another SoftLayer customer account's previously given access to provision CloudLayer Computing Instances
from an image template group. Template access should only be removed from the parent template group object,
not the child."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'denySharingAccess', accountId, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Virtual_Guest_Block_Device_Template_Group') -> bool:
        """Edit an image template group's name and note."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'editObject', templateObject, id=identifier)
        return data

    def findGcImagesByCurrentUser(self, dataCenters: str, regions: str) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Fetch a sorted collection of GC enabled cloudinit images for the account of the current active customer user."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'findGcImagesByCurrentUser', dataCenters, regions)
        return data

    def getAllAvailableCompatiblePlatformNames(self) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getAllAvailableCompatiblePlatformNames')
        return data

    def getBootMode(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getBootMode', id=identifier)
        return data

    def getCurrentCompatiblePlatformNames(self, identifier: int) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getCurrentCompatiblePlatformNames', id=identifier)
        return data

    def getDefaultBootMode(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getDefaultBootMode', id=identifier)
        return data

    def getEncryptionAttributes(self, identifier: int) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getEncryptionAttributes', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template_Group':
        """Retrieve a SoftLayer_Virtual_Guest_Block_Device_Template_Group record."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getObject', id=identifier)
        return data

    def getPublicCustomerOwnedImages(self) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Gets all public customer owned image templates that the user is allowed to see."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getPublicCustomerOwnedImages')
        return data

    def getPublicImages(self) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Gets all public image templates that the user is allowed to see."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getPublicImages')
        return data

    def getRiasAccount(self, secret: str) -> 'Container_Virtual_Guest_Block_Device_Template_Group_RiasAccount':
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getRiasAccount', secret)
        from SoftLayer.sltypes.Container_Virtual_Guest_Block_Device_Template_Group_RiasAccount import Container_Virtual_Guest_Block_Device_Template_Group_RiasAccount
        return data

    def getStorageLocations(self, identifier: int) -> list['Location']:
        """The available locations for public image storage."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getStorageLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getSupportedBootModes(self, identifier: int) -> list[str]:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getSupportedBootModes', id=identifier)
        return data

    def getTemplateDataCenterName(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getTemplateDataCenterName', id=identifier)
        return data

    def getVhdImportSoftwareDescriptions(self) -> list['Software_Description']:
        """Returns the software descriptions supported for VHD imports."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getVhdImportSoftwareDescriptions')
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def isByol(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isByol', id=identifier)
        return data

    def isByolCapableOperatingSystem(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isByolCapableOperatingSystem', id=identifier)
        return data

    def isByolOnlyOperatingSystem(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isByolOnlyOperatingSystem', id=identifier)
        return data

    def isCloudInit(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isCloudInit', id=identifier)
        return data

    def isCloudInitOnlyOperatingSystem(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isCloudInitOnlyOperatingSystem', id=identifier)
        return data

    def isEncrypted(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'isEncrypted', id=identifier)
        return data

    def permitSharingAccess(self, identifier: int, accountId: int) -> bool:
        """Permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image
template group. Template access should only be given to the parent template group object, not the child."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'permitSharingAccess', accountId, id=identifier)
        return data

    def removeCompatiblePlatforms(self, identifier: int, platformNames: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'removeCompatiblePlatforms', platformNames, id=identifier)
        return data

    def removeLocations(self, identifier: int, locations: 'Location') -> bool:
        """[[SoftLayer_Virtual_Guest_Block_Device]] can be made available in all storage locations. This method will
create transaction(s) to remove available locations from an archive image template."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'removeLocations', locations, id=identifier)
        return data

    def removeSupportedBootMode(self, identifier: int, bootMode: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'removeSupportedBootMode', bootMode, id=identifier)
        return data

    def setAvailableLocations(self, identifier: int, locations: 'Location') -> bool:
        """This method generates the necessary transaction(s) to set available locations for archived block devices."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'setAvailableLocations', locations, id=identifier)
        return data

    def setBootMode(self, identifier: int, newBootMode: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'setBootMode', newBootMode, id=identifier)
        return data

    def setCompatiblePlatforms(self, identifier: int, platformNames: str) -> bool:
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'setCompatiblePlatforms', platformNames, id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        """Set the tags for this template group."""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'setTags', tags, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAccountContacts(self, identifier: int) -> list['Account_Contact']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getAccountContacts', id=identifier)
        from SoftLayer.sltypes.Account_Contact import Account_Contact
        return data

    def getAccountReferences(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template_Group_Accounts']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getAccountReferences', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group_Accounts import Virtual_Guest_Block_Device_Template_Group_Accounts
        return data

    def getBlockDevices(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getBlockDevices', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template import Virtual_Guest_Block_Device_Template
        return data

    def getBlockDevicesDiskSpaceTotal(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getBlockDevicesDiskSpaceTotal', id=identifier)
        return data

    def getByolFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getByolFlag', id=identifier)
        return data

    def getChildren(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getChildren', id=identifier)
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDatacenters(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getDatacenters', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getFirstChild(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template_Group':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getFirstChild', id=identifier)
        return data

    def getFlexImageFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getFlexImageFlag', id=identifier)
        return data

    def getGlobalIdentifier(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getGlobalIdentifier', id=identifier)
        return data

    def getImageType(self, identifier: int) -> 'Virtual_Disk_Image_Type':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getImageType', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image_Type import Virtual_Disk_Image_Type
        return data

    def getImageTypeKeyName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getImageTypeKeyName', id=identifier)
        return data

    def getNextGenFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getNextGenFlag', id=identifier)
        return data

    def getParent(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template_Group':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getParent', id=identifier)
        return data

    def getRegion(self, identifier: int) -> 'Network_Service_Resource':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getRegion', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data

    def getRegions(self, identifier: int) -> list['Network_Service_Resource']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getRegions', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data

    def getSshKeys(self, identifier: int) -> list['Security_Ssh_Key']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getSshKeys', id=identifier)
        from SoftLayer.sltypes.Security_Ssh_Key import Security_Ssh_Key
        return data

    def getStatus(self, identifier: int) -> 'Virtual_Guest_Block_Device_Template_Group_Status':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group_Status import Virtual_Guest_Block_Device_Template_Group_Status
        return data

    def getStorageRepository(self, identifier: int) -> 'Virtual_Storage_Repository':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getStorageRepository', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository import Virtual_Storage_Repository
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Virtual_Guest_Block_Device_Template_Group', 'getTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data
