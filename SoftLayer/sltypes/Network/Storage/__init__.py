from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage(Entity):
    """The SoftLayer_Network_Storage data type contains general information regarding a Storage product such as
account id, access username and password, the Storage product type, and the server the Storage service is
associated with. Currently, only EVault backup storage has an associated server."""
    accountId: int
    capacityGb: int
    createDate: datetime
    guestId: int
    hardwareId: int
    hostId: int
    id_: int
    nasType: str
    notes: str
    password: str
    serviceProviderId: int
    storageTypeId: str
    upgradableFlag: bool
    username: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage'

    def allowAccessFromHardware(self, identifier: int, hardwareObjectTemplate: 'Hardware') -> bool:
        """Allow access to this volume from a specified SoftLayer_Hardware object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromHardware', hardwareObjectTemplate, id=identifier)
        return data

    def allowAccessFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def allowAccessFromHost(self, identifier: int, typeClassName: str, hostId: int) -> 'Network_Storage_Allowed_Host':
        """Allow access to this volume from a specified
[[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]]
object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromHost', typeClassName, hostId, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def allowAccessFromHostList(self, identifier: int, hostObjectTemplates: 'Container_Network_Storage_Host') -> list['Network_Storage_Allowed_Host']:
        """Allow access to this volume from multiple
[[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]]
objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromHostList', hostObjectTemplates, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def allowAccessFromIpAddress(self, identifier: int, ipAddressObjectTemplate: 'Network_Subnet_IpAddress') -> bool:
        """Allow access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromIpAddress', ipAddressObjectTemplate, id=identifier)
        return data

    def allowAccessFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def allowAccessFromSubnet(self, identifier: int, subnetObjectTemplate: 'Network_Subnet') -> bool:
        """Allow access to this volume from multiple SoftLayer_Network_Subnet objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromSubnet', subnetObjectTemplate, id=identifier)
        return data

    def allowAccessFromSubnetList(self, identifier: int, subnetObjectTemplates: 'Network_Subnet') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromSubnetList', subnetObjectTemplates, id=identifier)
        return data

    def allowAccessFromVirtualGuest(self, identifier: int, virtualGuestObjectTemplate: 'Virtual_Guest') -> bool:
        """Allow access to this volume from a specified SoftLayer_Virtual_Guest object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromVirtualGuest', virtualGuestObjectTemplate, id=identifier)
        return data

    def allowAccessFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """Allow access to this volume from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromHardware(self, identifier: int, hardwareObjectTemplate: 'Hardware') -> bool:
        """Allow access to this replicant volume from a specified SoftLayer_Hardware object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromHardware', hardwareObjectTemplate, id=identifier)
        return data

    def allowAccessToReplicantFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        """allow access to this volume's replica from multiple SoftLayer_Hardware objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromIpAddress(self, identifier: int, ipAddressObjectTemplate: 'Network_Subnet_IpAddress') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromIpAddress', ipAddressObjectTemplate, id=identifier)
        return data

    def allowAccessToReplicantFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        """allow access to this volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromSubnet(self, identifier: int, subnetObjectTemplate: 'Network_Subnet') -> bool:
        """Allow access to this replicant volume from multiple SoftLayer_Network_Subnet objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromSubnet', subnetObjectTemplate, id=identifier)
        return data

    def allowAccessToReplicantFromSubnetList(self, identifier: int, subnetObjectTemplates: 'Network_Subnet') -> bool:
        """allow access to this volume's replica from multiple SoftLayer_Network_Subnet objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromSubnetList', subnetObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromVirtualGuest(self, identifier: int, virtualGuestObjectTemplate: 'Virtual_Guest') -> bool:
        """Allow access to this replicant volume from a specified SoftLayer_Virtual_Guest object."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromVirtualGuest', virtualGuestObjectTemplate, id=identifier)
        return data

    def allowAccessToReplicantFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """allow access to this volume's replica from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'allowAccessToReplicantFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data

    def assignCredential(self, identifier: int, username: str) -> bool:
        """This method will assign an existing credential to the current volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'assignCredential', username, id=identifier)
        return data

    def assignNewCredential(self, identifier: int, type_: str) -> 'Network_Storage_Credential':
        """This method will set up a new credential for the remote storage volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'assignNewCredential', type, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Credential import Network_Storage_Credential
        return data

    def changePassword(self, username: str, currentPassword: str, newPassword: str) -> bool:
        """Change the password for a Storage/Virtual Server Storage account"""
        data = self.client.call('SoftLayer_Network_Storage', 'changePassword', username, currentPassword, newPassword)
        return data

    def collectBandwidth(self, identifier: int, type_: str, startDate: datetime, endDate: datetime) -> int:
        """Retrieve the bandwidth usage for the current billing cycle."""
        data = self.client.call('SoftLayer_Network_Storage', 'collectBandwidth', type, startDate, endDate, id=identifier)
        return data

    def collectBytesUsed(self, identifier: int) -> int:
        """Retrieve the number of bytes capacity currently in use on a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'collectBytesUsed', id=identifier)
        return data

    def convertCloneDependentToIndependent(self, identifier: int) -> bool:
        """Splits a clone from its parent allowing it to be an independent volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'convertCloneDependentToIndependent', id=identifier)
        return data

    def createFolder(self, identifier: int, folder: str) -> bool:
        """Create a new folder in the root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'createFolder', folder, id=identifier)
        return data

    def createOrUpdateLunId(self, identifier: int, lunId: int) -> 'Network_Storage_Property':
        """Creates or updates the LUN ID property on a volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'createOrUpdateLunId', lunId, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Property import Network_Storage_Property
        return data

    def createSnapshot(self, identifier: int, notes: str) -> 'Network_Storage':
        """Manually create a new snapshot of a storage volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'createSnapshot', notes, id=identifier)
        return data

    def deleteAllFiles(self, identifier: int) -> bool:
        """Delete all files within a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'deleteAllFiles', id=identifier)
        return data

    def deleteFile(self, identifier: int, fileId: str) -> bool:
        """Delete an individual file within a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'deleteFile', fileId, id=identifier)
        return data

    def deleteFiles(self, identifier: int, fileIds: str) -> bool:
        """Delete multiple files within a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'deleteFiles', fileIds, id=identifier)
        return data

    def deleteFolder(self, identifier: int, folder: str) -> bool:
        """Delete a folder in the root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'deleteFolder', folder, id=identifier)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a network storage volume"""
        data = self.client.call('SoftLayer_Network_Storage', 'deleteObject', id=identifier)
        return data

    def disableSnapshots(self, identifier: int, scheduleType: str) -> bool:
        """Disable snapshots of this Storage Volume on a schedule."""
        data = self.client.call('SoftLayer_Network_Storage', 'disableSnapshots', scheduleType, id=identifier)
        return data

    def disasterRecoveryFailoverToReplicant(self, identifier: int, replicantId: int) -> bool:
        """Failover an inaccessible block/file volume to its available replicant volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'disasterRecoveryFailoverToReplicant', replicantId, id=identifier)
        return data

    def downloadFile(self, identifier: int, fileId: str) -> 'Container_Utility_File_Entity':
        """Download a file from a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'downloadFile', fileId, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def editCredential(self, identifier: int, username: str, newPassword: str) -> bool:
        """This method will change the password of a credential created using the 'addNewCredential' method."""
        data = self.client.call('SoftLayer_Network_Storage', 'editCredential', username, newPassword, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Storage') -> bool:
        """Edit the password and/or notes for the Storage service"""
        data = self.client.call('SoftLayer_Network_Storage', 'editObject', templateObject, id=identifier)
        return data

    def enableSnapshots(self, identifier: int, scheduleType: str, retentionCount: int, minute: int, hour: int, dayOfWeek: str) -> bool:
        """Enable snapshots of this Storage Volume on a schedule."""
        data = self.client.call('SoftLayer_Network_Storage', 'enableSnapshots', scheduleType, retentionCount, minute, hour, dayOfWeek, id=identifier)
        return data

    def failbackFromReplicant(self, identifier: int) -> bool:
        """Failback from a volume replicant."""
        data = self.client.call('SoftLayer_Network_Storage', 'failbackFromReplicant', id=identifier)
        return data

    def failoverToReplicant(self, identifier: int, replicantId: int) -> bool:
        """Failover to a volume replicant."""
        data = self.client.call('SoftLayer_Network_Storage', 'failoverToReplicant', replicantId, id=identifier)
        return data

    def getAllFiles(self, identifier: int) -> list['Container_Utility_File_Entity']:
        """Retrieve a listing of all files in a Storage account's root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllFiles', id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getAllFilesByFilter(self, identifier: int, filter_: 'Container_Utility_File_Entity') -> list['Container_Utility_File_Entity']:
        """Retrieve a listing of all files matching the filter's criteria in a Storage account's root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllFilesByFilter', filter, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getAllowableHardware(self, identifier: int, filterHostname: str) -> list['Hardware']:
        """Return a list of SoftLayer_Hardware that can be authorized to this volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowableHardware', filterHostname, id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getAllowableIpAddresses(self, identifier: int, subnetId: int, filterIpAddress: str) -> list['Network_Subnet_IpAddress']:
        """Return a list of SoftLayer_Network_Subnet_IpAddress that can be authorized to this volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowableIpAddresses', subnetId, filterIpAddress, id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getAllowableSubnets(self, identifier: int, filterNetworkIdentifier: str) -> list['Network_Subnet']:
        """Return a list of SoftLayer_Network_Subnet that can be authorized to this volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowableSubnets', filterNetworkIdentifier, id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getAllowableVirtualGuests(self, identifier: int, filterHostname: str) -> list['Virtual_Guest']:
        """Return a list of SoftLayer_Virtual_Guest that can be authorized to this volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowableVirtualGuests', filterHostname, id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getAllowedHostsLimit(self, identifier: int) -> int:
        """Retrieves the total number of allowed hosts limit per volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedHostsLimit', id=identifier)
        return data

    def getByUsername(self, username: str, type_: str) -> list['Network_Storage']:
        """Retrieve network storage accounts by username."""
        data = self.client.call('SoftLayer_Network_Storage', 'getByUsername', username, type)
        return data

    def getCdnUrls(self, identifier: int) -> list['Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl']:
        data = self.client.call('SoftLayer_Network_Storage', 'getCdnUrls', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl import Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl
        return data

    def getClusterResource(self, identifier: int) -> 'Network_Service_Resource':
        data = self.client.call('SoftLayer_Network_Storage', 'getClusterResource', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data

    def getDuplicateConversionStatus(self, identifier: int) -> 'Container_Network_Storage_DuplicateConversionStatusInformation':
        """An API to fetch the percentage progress of conversion of a dependent"""
        data = self.client.call('SoftLayer_Network_Storage', 'getDuplicateConversionStatus', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_DuplicateConversionStatusInformation import Container_Network_Storage_DuplicateConversionStatusInformation
        return data

    def getFileBlockEncryptedLocations(self) -> list['Location']:
        """Returns a list of SoftLayer_Location_Datacenter objects corresponding to Datacenters in which File and Block
Storage Volumes with Encryption at Rest may be ordered."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFileBlockEncryptedLocations')
        from SoftLayer.sltypes.Location import Location
        return data

    def getFileByIdentifier(self, identifier: int, identifier: str) -> 'Container_Utility_File_Entity':
        """Retrieve an individual file's details."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFileByIdentifier', identifier, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getFileCount(self, identifier: int) -> int:
        """Retrieve the file number of files in a Virtual Server Storage account's root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFileCount', id=identifier)
        return data

    def getFileList(self, identifier: int, folder: str, path: str) -> list['Container_Utility_File_Entity']:
        """Retrieve list of files in a given folder for this account."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFileList', folder, path, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getFilePendingDeleteCount(self, identifier: int) -> int:
        """Retrieve the number of files pending deletion in a Storage account's recycle bin."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFilePendingDeleteCount', id=identifier)
        return data

    def getFilesPendingDelete(self, identifier: int) -> list['Container_Utility_File_Entity']:
        """Retrieve a list of files in a Storage account's recycle bin."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFilesPendingDelete', id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getFolderList(self, identifier: int) -> list['Container_Network_Storage_Hub_ObjectStorage_Folder']:
        """Retrieve a list of level 1 folders for this account."""
        data = self.client.call('SoftLayer_Network_Storage', 'getFolderList', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_Folder import Container_Network_Storage_Hub_ObjectStorage_Folder
        return data

    def getGraph(self, identifier: int, startDate: datetime, endDate: datetime, type_: str) -> 'Container_Bandwidth_GraphOutputs':
        """Retrieve a graph representing the bandwidth used by a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'getGraph', startDate, endDate, type, id=identifier)
        from SoftLayer.sltypes.Container_Bandwidth_GraphOutputs import Container_Bandwidth_GraphOutputs
        return data

    def getMaximumExpansionSize(self, identifier: int) -> int:
        """Returns the maximum volume expansion size in GB."""
        data = self.client.call('SoftLayer_Network_Storage', 'getMaximumExpansionSize', id=identifier)
        return data

    def getNetworkConnectionDetails(self, identifier: int) -> 'Container_Network_Storage_NetworkConnectionInformation':
        """Retrieve network connection details for complex network storage volumes."""
        data = self.client.call('SoftLayer_Network_Storage', 'getNetworkConnectionDetails', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_NetworkConnectionInformation import Container_Network_Storage_NetworkConnectionInformation
        return data

    def getNetworkMountAddress(self, identifier: int) -> str:
        """Displays the mount path of a storage volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getNetworkMountAddress', id=identifier)
        return data

    def getNetworkMountPath(self, identifier: int) -> str:
        """Displays the mount path of a storage volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getNetworkMountPath', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Storage':
        """Retrieve a SoftLayer_Network_Storage record."""
        data = self.client.call('SoftLayer_Network_Storage', 'getObject', id=identifier)
        return data

    def getObjectStorageConnectionInformation(self) -> list['Container_Network_Service_Resource_ObjectStorage_ConnectionInformation']:
        """Retrieve all object storage details for connection"""
        data = self.client.call('SoftLayer_Network_Storage', 'getObjectStorageConnectionInformation')
        from SoftLayer.sltypes.Container_Network_Service_Resource_ObjectStorage_ConnectionInformation import Container_Network_Service_Resource_ObjectStorage_ConnectionInformation
        return data

    def getObjectsByCredential(self, credentialObject: 'Network_Storage_Credential') -> list['Network_Storage']:
        """Retrieve network storage accounts by SoftLayer_Network_Storage_Credential object."""
        data = self.client.call('SoftLayer_Network_Storage', 'getObjectsByCredential', credentialObject)
        return data

    def getRecycleBinFileByIdentifier(self, identifier: int, fileId: str) -> 'Container_Utility_File_Entity':
        """Retrieve all files that are in the recycle bin (pending delete).  This method is only used for Virtual Server
Storage accounts at moment but may expanded to other Storage types in the future."""
        data = self.client.call('SoftLayer_Network_Storage', 'getRecycleBinFileByIdentifier', fileId, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getRemainingAllowedHosts(self, identifier: int) -> int:
        """Retrieves the remaining number of allowed hosts per volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getRemainingAllowedHosts', id=identifier)
        return data

    def getRemainingAllowedHostsForReplicant(self, identifier: int) -> int:
        """Retrieves the remaining number of allowed hosts for a volume's replicant."""
        data = self.client.call('SoftLayer_Network_Storage', 'getRemainingAllowedHostsForReplicant', id=identifier)
        return data

    def getReplicationTimestamp(self, identifier: int) -> str:
        """An API call to fetch the last timestamp of the replication process"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicationTimestamp', id=identifier)
        return data

    def getSnapshotsForVolume(self, identifier: int) -> list['Network_Storage']:
        """Retrieves a list oƒf snapshots for a given volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotsForVolume', id=identifier)
        return data

    def getStorageGroupsNetworkConnectionDetails(self, identifier: int) -> list['Container_Network_Storage_NetworkConnectionInformation']:
        data = self.client.call('SoftLayer_Network_Storage', 'getStorageGroupsNetworkConnectionDetails', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_NetworkConnectionInformation import Container_Network_Storage_NetworkConnectionInformation
        return data

    def getTargetIpAddresses(self, identifier: int) -> list[str]:
        data = self.client.call('SoftLayer_Network_Storage', 'getTargetIpAddresses', id=identifier)
        return data

    def getValidReplicationTargetDatacenterLocations(self, identifier: int) -> list['Location']:
        data = self.client.call('SoftLayer_Network_Storage', 'getValidReplicationTargetDatacenterLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getVolumeCountLimits(self) -> list['Container_Network_Storage_DataCenterLimits_VolumeCountLimitContainer']:
        """Retrieves an array of volume count limits per location and globally."""
        data = self.client.call('SoftLayer_Network_Storage', 'getVolumeCountLimits')
        from SoftLayer.sltypes.Container_Network_Storage_DataCenterLimits_VolumeCountLimitContainer import Container_Network_Storage_DataCenterLimits_VolumeCountLimitContainer
        return data

    def getVolumeDuplicateParameters(self, identifier: int) -> 'Container_Network_Storage_VolumeDuplicateParameters':
        data = self.client.call('SoftLayer_Network_Storage', 'getVolumeDuplicateParameters', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_VolumeDuplicateParameters import Container_Network_Storage_VolumeDuplicateParameters
        return data

    def immediateFailoverToReplicant(self, identifier: int, replicantId: int) -> bool:
        """Immediate Failover to a volume replicant."""
        data = self.client.call('SoftLayer_Network_Storage', 'immediateFailoverToReplicant', replicantId, id=identifier)
        return data

    def initiateOriginVolumeReclaim(self, identifier: int) -> str:
        """Initiates Origin Volume Reclaim to delete volume from NetApp."""
        data = self.client.call('SoftLayer_Network_Storage', 'initiateOriginVolumeReclaim', id=identifier)
        return data

    def initiateVolumeCutover(self, identifier: int) -> str:
        """Initiates Volume Cutover to remove access from the old volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'initiateVolumeCutover', id=identifier)
        return data

    def isBlockingOperationInProgress(self, identifier: int, exemptStatusKeyNames: str) -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'isBlockingOperationInProgress', exemptStatusKeyNames, id=identifier)
        return data

    def isDuplicateReadyForSnapshot(self, identifier: int) -> bool:
        """Displays the if clone snapshots can be ordered."""
        data = self.client.call('SoftLayer_Network_Storage', 'isDuplicateReadyForSnapshot', id=identifier)
        return data

    def isDuplicateReadyToMount(self, identifier: int) -> bool:
        """Displays the status of a clone mount."""
        data = self.client.call('SoftLayer_Network_Storage', 'isDuplicateReadyToMount', id=identifier)
        return data

    def isVolumeActive(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'isVolumeActive', id=identifier)
        return data

    def refreshDependentDuplicate(self, identifier: int, snapshotId: int) -> bool:
        """Refreshes a duplicate volume with a snapshot taken from its parent. This is deprecated now."""
        data = self.client.call('SoftLayer_Network_Storage', 'refreshDependentDuplicate', snapshotId, id=identifier)
        return data

    def refreshDuplicate(self, identifier: int, snapshotId: int, forceRefresh: bool) -> bool:
        """Refreshes any duplicate volume with a snapshot taken from its parent."""
        data = self.client.call('SoftLayer_Network_Storage', 'refreshDuplicate', snapshotId, forceRefresh, id=identifier)
        return data

    def removeAccessFromHardware(self, identifier: int, hardwareObjectTemplate: 'Hardware') -> bool:
        """Remove access to this volume from a specified SoftLayer_Hardware object."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromHardware', hardwareObjectTemplate, id=identifier)
        return data

    def removeAccessFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        """Remove access to this volume from multiple SoftLayer_Hardware objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def removeAccessFromHost(self, identifier: int, typeClassName: str, hostId: int) -> 'Network_Storage_Allowed_Host':
        """Remove access to this volume from a specified
[[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]]
object."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromHost', typeClassName, hostId, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def removeAccessFromHostList(self, identifier: int, hostObjectTemplates: 'Container_Network_Storage_Host') -> list['Network_Storage_Allowed_Host']:
        """Remove access to this volume from multiple
[[SoftLayer_Hardware|SoftLayer_Virtual_Guest|SoftLayer_Network_Subnet|SoftLayer_Network_Subnet_IpAddress]]
objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromHostList', hostObjectTemplates, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def removeAccessFromIpAddress(self, identifier: int, ipAddressObjectTemplate: 'Network_Subnet_IpAddress') -> bool:
        """Remove access to this volume from a specified SoftLayer_Network_Subnet_IpAddress object."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromIpAddress', ipAddressObjectTemplate, id=identifier)
        return data

    def removeAccessFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def removeAccessFromSubnet(self, identifier: int, subnetObjectTemplate: 'Network_Subnet') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromSubnet', subnetObjectTemplate, id=identifier)
        return data

    def removeAccessFromSubnetList(self, identifier: int, subnetObjectTemplates: 'Network_Subnet') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromSubnetList', subnetObjectTemplates, id=identifier)
        return data

    def removeAccessFromVirtualGuest(self, identifier: int, virtualGuestObjectTemplate: 'Virtual_Guest') -> bool:
        """Remove access to this volume from a specified SoftLayer_Virtual_Guest object."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromVirtualGuest', virtualGuestObjectTemplate, id=identifier)
        return data

    def removeAccessFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """Remove access to this volume from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        """Remove access to this volume's replica from multiple SoftLayer_Hardware objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessToReplicantFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        """Remove access to this replica volume's replica from multiple SoftLayer_Network_Subnet_IpAddress objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessToReplicantFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromSubnet(self, identifier: int, subnetObjectTemplate: 'Network_Subnet') -> bool:
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessToReplicantFromSubnet', subnetObjectTemplate, id=identifier)
        return data

    def removeAccessToReplicantFromSubnetList(self, identifier: int, subnetObjectTemplates: 'Network_Subnet') -> bool:
        """Remove access to this volume's replica from multiple SoftLayer_Network_Subnet objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessToReplicantFromSubnetList', subnetObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """Remove access to this volume's replica from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeAccessToReplicantFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data

    def removeCredential(self, identifier: int, username: str) -> bool:
        """This method will remove a credential from the current volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'removeCredential', username, id=identifier)
        return data

    def restoreFile(self, identifier: int, fileId: str) -> 'Container_Utility_File_Entity':
        """Restore access to an individual file in a Storage account."""
        data = self.client.call('SoftLayer_Network_Storage', 'restoreFile', fileId, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def restoreFromSnapshot(self, identifier: int, snapshotId: int) -> bool:
        """Restore from a volume snapshot."""
        data = self.client.call('SoftLayer_Network_Storage', 'restoreFromSnapshot', snapshotId, id=identifier)
        return data

    def sendPasswordReminderEmail(self, username: str) -> bool:
        """Email the password for the Storage account to the master user."""
        data = self.client.call('SoftLayer_Network_Storage', 'sendPasswordReminderEmail', username)
        return data

    def setMountable(self, identifier: int, mountable: bool) -> bool:
        """Enable or disable mounting of a Storage volume."""
        data = self.client.call('SoftLayer_Network_Storage', 'setMountable', mountable, id=identifier)
        return data

    def setSnapshotAllocation(self, identifier: int, capacityGb: int) -> None:
        data = self.client.call('SoftLayer_Network_Storage', 'setSnapshotAllocation', capacityGb, id=identifier)
        return data

    def setSnapshotNotification(self, identifier: int, notificationFlag: bool) -> None:
        """Function to enable/disable snapshot warning notification."""
        data = self.client.call('SoftLayer_Network_Storage', 'setSnapshotNotification', notificationFlag, id=identifier)
        return data

    def upgradeVolumeCapacity(self, identifier: int, itemId: int) -> bool:
        """Edit the Storage volume to a different package"""
        data = self.client.call('SoftLayer_Network_Storage', 'upgradeVolumeCapacity', itemId, id=identifier)
        return data

    def uploadFile(self, identifier: int, file: 'Container_Utility_File_Entity') -> 'Container_Utility_File_Entity':
        """Upload a file to a Storage account's root directory."""
        data = self.client.call('SoftLayer_Network_Storage', 'uploadFile', file, id=identifier)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def validateHostsAccess(self, identifier: int, hostObjectTemplates: 'Container_Network_Storage_Host') -> list['Container_Network_Storage_HostsGatewayInformation']:
        """An API to check if the hosts provided are behind gateway or not from"""
        data = self.client.call('SoftLayer_Network_Storage', 'validateHostsAccess', hostObjectTemplates, id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_HostsGatewayInformation import Container_Network_Storage_HostsGatewayInformation
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAccountPassword(self, identifier: int) -> 'Account_Password':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAccountPassword', id=identifier)
        from SoftLayer.sltypes.Account_Password import Account_Password
        return data

    def getActiveTransactions(self, identifier: int) -> list['Provisioning_Version1_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getActiveTransactions', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getAllowDisasterRecoveryFailback(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowDisasterRecoveryFailback', id=identifier)
        return data

    def getAllowDisasterRecoveryFailover(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowDisasterRecoveryFailover', id=identifier)
        return data

    def getAllowedHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getAllowedIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getAllowedReplicationHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedReplicationHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getAllowedReplicationIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedReplicationIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getAllowedReplicationSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedReplicationSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getAllowedReplicationVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedReplicationVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getAllowedSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getAllowedVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getAllowedVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getBillingItemCategory(self, identifier: int) -> 'Product_Item_Category':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getBillingItemCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getBytesUsed(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getBytesUsed', id=identifier)
        return data

    def getCreationScheduleId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getCreationScheduleId', id=identifier)
        return data

    def getCredentials(self, identifier: int) -> list['Network_Storage_Credential']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getCredentials', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Credential import Network_Storage_Credential
        return data

    def getDailySchedule(self, identifier: int) -> 'Network_Storage_Schedule':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getDailySchedule', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data

    def getDependentDuplicate(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getDependentDuplicate', id=identifier)
        return data

    def getDependentDuplicates(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getDependentDuplicates', id=identifier)
        return data

    def getEvents(self, identifier: int) -> list['Network_Storage_Event']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getEvents', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Event import Network_Storage_Event
        return data

    def getFailbackNotAllowed(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getFailbackNotAllowed', id=identifier)
        return data

    def getFailoverNotAllowed(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getFailoverNotAllowed', id=identifier)
        return data

    def getFileNetworkMountAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getFileNetworkMountAddress', id=identifier)
        return data

    def getFixReplicationCurrentStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getFixReplicationCurrentStatus', id=identifier)
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHasEncryptionAtRest(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getHasEncryptionAtRest', id=identifier)
        return data

    def getHourlySchedule(self, identifier: int) -> 'Network_Storage_Schedule':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getHourlySchedule', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data

    def getIntervalSchedule(self, identifier: int) -> 'Network_Storage_Schedule':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIntervalSchedule', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data

    def getIops(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIops', id=identifier)
        return data

    def getIsConvertToIndependentTransactionInProgress(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsConvertToIndependentTransactionInProgress', id=identifier)
        return data

    def getIsDependentDuplicateProvisionCompleted(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsDependentDuplicateProvisionCompleted', id=identifier)
        return data

    def getIsInDedicatedServiceResource(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsInDedicatedServiceResource', id=identifier)
        return data

    def getIsMagneticStorage(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsMagneticStorage', id=identifier)
        return data

    def getIsProvisionInProgress(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsProvisionInProgress', id=identifier)
        return data

    def getIsReadyForSnapshot(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsReadyForSnapshot', id=identifier)
        return data

    def getIsReadyToMount(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIsReadyToMount', id=identifier)
        return data

    def getIscsiLuns(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIscsiLuns', id=identifier)
        return data

    def getIscsiReplicatingVolume(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIscsiReplicatingVolume', id=identifier)
        return data

    def getIscsiTargetIpAddresses(self, identifier: int) -> list[str]:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getIscsiTargetIpAddresses', id=identifier)
        return data

    def getLunId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getLunId', id=identifier)
        return data

    def getManualSnapshots(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getManualSnapshots', id=identifier)
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getMountPath(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getMountPath', id=identifier)
        return data

    def getMountableFlag(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getMountableFlag', id=identifier)
        return data

    def getMoveAndSplitStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getMoveAndSplitStatus', id=identifier)
        return data

    def getNotificationSubscribers(self, identifier: int) -> list['Notification_User_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getNotificationSubscribers', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
        return data

    def getOriginalSnapshotName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOriginalSnapshotName', id=identifier)
        return data

    def getOriginalVolumeId(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOriginalVolumeId', id=identifier)
        return data

    def getOriginalVolumeName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOriginalVolumeName', id=identifier)
        return data

    def getOriginalVolumeSize(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOriginalVolumeSize', id=identifier)
        return data

    def getOsType(self, identifier: int) -> 'Network_Storage_Iscsi_OS_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOsType', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Iscsi_OS_Type import Network_Storage_Iscsi_OS_Type
        return data

    def getOsTypeId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getOsTypeId', id=identifier)
        return data

    def getParentPartnerships(self, identifier: int) -> list['Network_Storage_Partnership']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getParentPartnerships', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Partnership import Network_Storage_Partnership
        return data

    def getParentVolume(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getParentVolume', id=identifier)
        return data

    def getPartnerships(self, identifier: int) -> list['Network_Storage_Partnership']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getPartnerships', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Partnership import Network_Storage_Partnership
        return data

    def getPermissionsGroups(self, identifier: int) -> list['Network_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getPermissionsGroups', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group import Network_Storage_Group
        return data

    def getProperties(self, identifier: int) -> list['Network_Storage_Property']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getProperties', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Property import Network_Storage_Property
        return data

    def getProvisionedIops(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getProvisionedIops', id=identifier)
        return data

    def getReplicatingLuns(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicatingLuns', id=identifier)
        return data

    def getReplicatingVolume(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicatingVolume', id=identifier)
        return data

    def getReplicationEvents(self, identifier: int) -> list['Network_Storage_Event']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicationEvents', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Event import Network_Storage_Event
        return data

    def getReplicationPartners(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicationPartners', id=identifier)
        return data

    def getReplicationSchedule(self, identifier: int) -> 'Network_Storage_Schedule':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicationSchedule', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data

    def getReplicationStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getReplicationStatus', id=identifier)
        return data

    def getSchedules(self, identifier: int) -> list['Network_Storage_Schedule']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSchedules', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data

    def getServiceResource(self, identifier: int) -> 'Network_Service_Resource':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getServiceResource', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data

    def getServiceResourceBackendIpAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getServiceResourceBackendIpAddress', id=identifier)
        return data

    def getServiceResourceName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getServiceResourceName', id=identifier)
        return data

    def getSnapshotCapacityGb(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotCapacityGb', id=identifier)
        return data

    def getSnapshotCreationTimestamp(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotCreationTimestamp', id=identifier)
        return data

    def getSnapshotDeletionThresholdPercentage(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotDeletionThresholdPercentage', id=identifier)
        return data

    def getSnapshotNotificationStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotNotificationStatus', id=identifier)
        return data

    def getSnapshotSizeBytes(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotSizeBytes', id=identifier)
        return data

    def getSnapshotSpaceAvailable(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshotSpaceAvailable', id=identifier)
        return data

    def getSnapshots(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getSnapshots', id=identifier)
        return data

    def getStaasVersion(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getStaasVersion', id=identifier)
        return data

    def getStorageGroups(self, identifier: int) -> list['Network_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getStorageGroups', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group import Network_Storage_Group
        return data

    def getStorageTierLevel(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getStorageTierLevel', id=identifier)
        return data

    def getStorageType(self, identifier: int) -> 'Network_Storage_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getStorageType', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Type import Network_Storage_Type
        return data

    def getTotalBytesUsed(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getTotalBytesUsed', id=identifier)
        return data

    def getTotalScheduleSnapshotRetentionCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getTotalScheduleSnapshotRetentionCount', id=identifier)
        return data

    def getUsageNotification(self, identifier: int) -> 'Notification':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getUsageNotification', id=identifier)
        from SoftLayer.sltypes.Notification import Notification
        return data

    def getVendorName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getVendorName', id=identifier)
        return data

    def getVirtualGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getVirtualGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVolumeHistory(self, identifier: int) -> list['Network_Storage_History']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getVolumeHistory', id=identifier)
        from SoftLayer.sltypes.Network_Storage_History import Network_Storage_History
        return data

    def getVolumeStatus(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getVolumeStatus', id=identifier)
        return data

    def getWebccAccount(self, identifier: int) -> 'Account_Password':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getWebccAccount', id=identifier)
        from SoftLayer.sltypes.Account_Password import Account_Password
        return data

    def getWeeklySchedule(self, identifier: int) -> 'Network_Storage_Schedule':
        """"""
        data = self.client.call('SoftLayer_Network_Storage', 'getWeeklySchedule', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Schedule import Network_Storage_Schedule
        return data
