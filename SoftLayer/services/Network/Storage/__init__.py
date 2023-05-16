# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage'
        self.client = client

    def allowAccessFromHardware(
        self,
        hardwareObjectTemplate: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromHardware',
            hardwareObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessFromHardwareList(
        self,
        hardwareObjectTemplates: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromHardwareList',
            hardwareObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessFromHost(
        self,
        typeClassName: str,
        hostId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'allowAccessFromHost',
            typeClassName,
            hostId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def allowAccessFromHostList(
        self,
        hostObjectTemplates: 'SoftLayer_Container_Network_Storage_Host',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'allowAccessFromHostList',
            hostObjectTemplates,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def allowAccessFromIpAddress(
        self,
        ipAddressObjectTemplate: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromIpAddress',
            ipAddressObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessFromIpAddressList(
        self,
        ipAddressObjectTemplates: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromIpAddressList',
            ipAddressObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessFromSubnet(
        self,
        subnetObjectTemplate: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromSubnet',
            subnetObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessFromSubnetList(
        self,
        subnetObjectTemplates: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromSubnetList',
            subnetObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromVirtualGuest',
            virtualGuestObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromVirtualGuestList',
            virtualGuestObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromHardware(
        self,
        hardwareObjectTemplate: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromHardware',
            hardwareObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromHardwareList(
        self,
        hardwareObjectTemplates: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromHardwareList',
            hardwareObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromIpAddress(
        self,
        ipAddressObjectTemplate: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromIpAddress',
            ipAddressObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromIpAddressList(
        self,
        ipAddressObjectTemplates: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromIpAddressList',
            ipAddressObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromSubnet(
        self,
        subnetObjectTemplate: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromSubnet',
            subnetObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromSubnetList(
        self,
        subnetObjectTemplates: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromSubnetList',
            subnetObjectTemplates,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromVirtualGuest',
            virtualGuestObjectTemplate,
            id=identifier
        )
        
        return data


    def allowAccessToReplicantFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromVirtualGuestList',
            virtualGuestObjectTemplates,
            id=identifier
        )
        
        return data


    def assignCredential(
        self,
        username: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'assignCredential',
            username,
            id=identifier
        )
        
        return data


    def assignNewCredential(
        self,
        type: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Credential':

        data = self.client.call(
            self.service,
            'assignNewCredential',
            type,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def changePassword(
        self,
        username: str,
        currentPassword: str,
        newPassword: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'changePassword',
            username,
            currentPassword,
            newPassword
        )
        
        return data


    def collectBandwidth(
        self,
        type: str,
        startDate: str,
        endDate: str,
        identifier: int
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'collectBandwidth',
            type,
            startDate,
            endDate,
            id=identifier
        )
        
        return data


    def collectBytesUsed(
        self,
        identifier: int
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'collectBytesUsed',
            id=identifier
        )
        
        return data


    def convertCloneDependentToIndependent(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'convertCloneDependentToIndependent',
            id=identifier
        )
        
        return data


    def createFolder(
        self,
        folder: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createFolder',
            folder,
            id=identifier
        )
        
        return data


    def createOrUpdateLunId(
        self,
        lunId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Property':

        data = self.client.call(
            self.service,
            'createOrUpdateLunId',
            lunId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Property import Property
        return Property(data)


    def createSnapshot(
        self,
        notes: str,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'createSnapshot',
            notes,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def deleteAllFiles(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteAllFiles',
            id=identifier
        )
        
        return data


    def deleteFile(
        self,
        fileId: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFile',
            fileId,
            id=identifier
        )
        
        return data


    def deleteFiles(
        self,
        fileIds: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFiles',
            fileIds,
            id=identifier
        )
        
        return data


    def deleteFolder(
        self,
        folder: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFolder',
            folder,
            id=identifier
        )
        
        return data


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def disableSnapshots(
        self,
        scheduleType: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disableSnapshots',
            scheduleType,
            id=identifier
        )
        
        return data


    def disasterRecoveryFailoverToReplicant(
        self,
        replicantId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disasterRecoveryFailoverToReplicant',
            replicantId,
            id=identifier
        )
        
        return data


    def downloadFile(
        self,
        fileId: str,
        identifier: int
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'downloadFile',
            fileId,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def editCredential(
        self,
        username: str,
        newPassword: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editCredential',
            username,
            newPassword,
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def enableSnapshots(
        self,
        scheduleType: str,
        retentionCount: int,
        minute: int,
        hour: int,
        dayOfWeek: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enableSnapshots',
            scheduleType,
            retentionCount,
            minute,
            hour,
            dayOfWeek,
            id=identifier
        )
        
        return data


    def failbackFromReplicant(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'failbackFromReplicant',
            id=identifier
        )
        
        return data


    def failoverToReplicant(
        self,
        replicantId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'failoverToReplicant',
            replicantId,
            id=identifier
        )
        
        return data


    def getAllFiles(
        self,
        identifier: int,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getAllFiles',
            id=identifier,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getAllFilesByFilter(
        self,
        filter: 'SoftLayer_Container_Utility_File_Entity',
        identifier: int,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getAllFilesByFilter',
            filter,
            id=identifier,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getAllowableHardware(
        self,
        filterHostname: str,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowableHardware',
            filterHostname,
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getAllowableIpAddresses(
        self,
        subnetId: int,
        filterIpAddress: str,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowableIpAddresses',
            subnetId,
            filterIpAddress,
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowableSubnets(
        self,
        filterNetworkIdentifier: str,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowableSubnets',
            filterNetworkIdentifier,
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowableVirtualGuests(
        self,
        filterHostname: str,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowableVirtualGuests',
            filterHostname,
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getAllowedHostsLimit(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAllowedHostsLimit',
            id=identifier
        )
        
        return data


    def getByUsername(
        self,
        username: str,
        type: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getByUsername',
            username,
            type,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getCdnUrls(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl]':

        data = self.client.call(
            self.service,
            'getCdnUrls',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.ContentDeliveryUrl import ContentDeliveryUrl
        return ContentDeliveryUrl(data)


    def getClusterResource(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getClusterResource',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getDuplicateConversionStatus(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Storage_DuplicateConversionStatusInformation':

        data = self.client.call(
            self.service,
            'getDuplicateConversionStatus',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.DuplicateConversionStatusInformation import DuplicateConversionStatusInformation
        return DuplicateConversionStatusInformation(data)


    def getFileBlockEncryptedLocations(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getFileBlockEncryptedLocations',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getFileByIdentifier(
        self,
        identifier: str,
        identifier: int
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'getFileByIdentifier',
            identifier,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFileCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getFileCount',
            id=identifier
        )
        
        return data


    def getFileList(
        self,
        folder: str,
        path: str,
        identifier: int
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getFileList',
            folder,
            path,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFilePendingDeleteCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getFilePendingDeleteCount',
            id=identifier
        )
        
        return data


    def getFilesPendingDelete(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getFilesPendingDelete',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFolderList(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Folder]':

        data = self.client.call(
            self.service,
            'getFolderList',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Folder import Folder
        return Folder(data)


    def getGraph(
        self,
        startDate: str,
        endDate: str,
        type: str,
        identifier: int
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getGraph',
            startDate,
            endDate,
            type,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getMaximumExpansionSize(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getMaximumExpansionSize',
            id=identifier
        )
        
        return data


    def getNetworkConnectionDetails(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Storage_NetworkConnectionInformation':

        data = self.client.call(
            self.service,
            'getNetworkConnectionDetails',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


    def getNetworkMountAddress(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNetworkMountAddress',
            id=identifier
        )
        
        return data


    def getNetworkMountPath(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNetworkMountPath',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getObjectStorageConnectionInformation(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Service_Resource_ObjectStorage_ConnectionInformation]':

        data = self.client.call(
            self.service,
            'getObjectStorageConnectionInformation',
            
        )
        from SoftLayer.datatypes.Container.Network.Service.Resource.ObjectStorage.ConnectionInformation import ConnectionInformation
        return ConnectionInformation(data)


    def getObjectsByCredential(
        self,
        credentialObject: 'SoftLayer_Network_Storage_Credential',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getObjectsByCredential',
            credentialObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getRecycleBinFileByIdentifier(
        self,
        fileId: str,
        identifier: int
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'getRecycleBinFileByIdentifier',
            fileId,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getRemainingAllowedHosts(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getRemainingAllowedHosts',
            id=identifier
        )
        
        return data


    def getRemainingAllowedHostsForReplicant(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getRemainingAllowedHostsForReplicant',
            id=identifier
        )
        
        return data


    def getReplicationTimestamp(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReplicationTimestamp',
            id=identifier
        )
        
        return data


    def getSnapshotsForVolume(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getSnapshotsForVolume',
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getStorageGroupsNetworkConnectionDetails(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_NetworkConnectionInformation]':

        data = self.client.call(
            self.service,
            'getStorageGroupsNetworkConnectionDetails',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


    def getTargetIpAddresses(
        self,
        identifier: int
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getTargetIpAddresses',
            id=identifier
        )
        
        return data


    def getValidReplicationTargetDatacenterLocations(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getValidReplicationTargetDatacenterLocations',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getVolumeCountLimits(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Storage_DataCenterLimits_VolumeCountLimitContainer]':

        data = self.client.call(
            self.service,
            'getVolumeCountLimits',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.DataCenterLimits.VolumeCountLimitContainer import VolumeCountLimitContainer
        return VolumeCountLimitContainer(data)


    def getVolumeDuplicateParameters(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Storage_VolumeDuplicateParameters':

        data = self.client.call(
            self.service,
            'getVolumeDuplicateParameters',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.VolumeDuplicateParameters import VolumeDuplicateParameters
        return VolumeDuplicateParameters(data)


    def immediateFailoverToReplicant(
        self,
        replicantId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'immediateFailoverToReplicant',
            replicantId,
            id=identifier
        )
        
        return data


    def initiateOriginVolumeReclaim(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'initiateOriginVolumeReclaim',
            id=identifier
        )
        
        return data


    def initiateVolumeCutover(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'initiateVolumeCutover',
            id=identifier
        )
        
        return data


    def isBlockingOperationInProgress(
        self,
        exemptStatusKeyNames: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isBlockingOperationInProgress',
            exemptStatusKeyNames,
            id=identifier
        )
        
        return data


    def isDuplicateReadyForSnapshot(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isDuplicateReadyForSnapshot',
            id=identifier
        )
        
        return data


    def isDuplicateReadyToMount(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isDuplicateReadyToMount',
            id=identifier
        )
        
        return data


    def isVolumeActive(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isVolumeActive',
            id=identifier
        )
        
        return data


    def refreshDependentDuplicate(
        self,
        snapshotId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshDependentDuplicate',
            snapshotId,
            id=identifier
        )
        
        return data


    def refreshDuplicate(
        self,
        snapshotId: int,
        forceRefresh: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshDuplicate',
            snapshotId,
            forceRefresh,
            id=identifier
        )
        
        return data


    def removeAccessFromHardware(
        self,
        hardwareObjectTemplate: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromHardware',
            hardwareObjectTemplate,
            id=identifier
        )
        
        return data


    def removeAccessFromHardwareList(
        self,
        hardwareObjectTemplates: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromHardwareList',
            hardwareObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessFromHost(
        self,
        typeClassName: str,
        hostId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'removeAccessFromHost',
            typeClassName,
            hostId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def removeAccessFromHostList(
        self,
        hostObjectTemplates: 'SoftLayer_Container_Network_Storage_Host',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'removeAccessFromHostList',
            hostObjectTemplates,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def removeAccessFromIpAddress(
        self,
        ipAddressObjectTemplate: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromIpAddress',
            ipAddressObjectTemplate,
            id=identifier
        )
        
        return data


    def removeAccessFromIpAddressList(
        self,
        ipAddressObjectTemplates: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromIpAddressList',
            ipAddressObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessFromSubnet(
        self,
        subnetObjectTemplate: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromSubnet',
            subnetObjectTemplate,
            id=identifier
        )
        
        return data


    def removeAccessFromSubnetList(
        self,
        subnetObjectTemplates: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromSubnetList',
            subnetObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromVirtualGuest',
            virtualGuestObjectTemplate,
            id=identifier
        )
        
        return data


    def removeAccessFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromVirtualGuestList',
            virtualGuestObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessToReplicantFromHardwareList(
        self,
        hardwareObjectTemplates: 'SoftLayer_Hardware',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromHardwareList',
            hardwareObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessToReplicantFromIpAddressList(
        self,
        ipAddressObjectTemplates: 'SoftLayer_Network_Subnet_IpAddress',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromIpAddressList',
            ipAddressObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessToReplicantFromSubnet(
        self,
        subnetObjectTemplate: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromSubnet',
            subnetObjectTemplate,
            id=identifier
        )
        
        return data


    def removeAccessToReplicantFromSubnetList(
        self,
        subnetObjectTemplates: 'SoftLayer_Network_Subnet',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromSubnetList',
            subnetObjectTemplates,
            id=identifier
        )
        
        return data


    def removeAccessToReplicantFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: 'SoftLayer_Virtual_Guest',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromVirtualGuestList',
            virtualGuestObjectTemplates,
            id=identifier
        )
        
        return data


    def removeCredential(
        self,
        username: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeCredential',
            username,
            id=identifier
        )
        
        return data


    def restoreFile(
        self,
        fileId: str,
        identifier: int
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'restoreFile',
            fileId,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def restoreFromSnapshot(
        self,
        snapshotId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreFromSnapshot',
            snapshotId,
            id=identifier
        )
        
        return data


    def sendPasswordReminderEmail(
        self,
        username: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendPasswordReminderEmail',
            username
        )
        
        return data


    def setMountable(
        self,
        mountable: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setMountable',
            mountable,
            id=identifier
        )
        
        return data


    def setSnapshotAllocation(
        self,
        capacityGb: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setSnapshotAllocation',
            capacityGb,
            id=identifier
        )
        
        return data


    def setSnapshotNotification(
        self,
        notificationFlag: bool,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setSnapshotNotification',
            notificationFlag,
            id=identifier
        )
        
        return data


    def upgradeVolumeCapacity(
        self,
        itemId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'upgradeVolumeCapacity',
            itemId,
            id=identifier
        )
        
        return data


    def uploadFile(
        self,
        file: 'SoftLayer_Container_Utility_File_Entity',
        identifier: int
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'uploadFile',
            file,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def validateHostsAccess(
        self,
        hostObjectTemplates: 'SoftLayer_Container_Network_Storage_Host',
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Storage_HostsGatewayInformation]':

        data = self.client.call(
            self.service,
            'validateHostsAccess',
            hostObjectTemplates,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.HostsGatewayInformation import HostsGatewayInformation
        return HostsGatewayInformation(data)


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


    def getAccountPassword(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Password':

        data = self.client.call(
            self.service,
            'getAccountPassword',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Password import Password
        return Password(data)


    def getActiveTransactions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':

        data = self.client.call(
            self.service,
            'getActiveTransactions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAllowDisasterRecoveryFailback(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAllowDisasterRecoveryFailback',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllowDisasterRecoveryFailover(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAllowDisasterRecoveryFailover',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllowedHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowedHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getAllowedIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowedIpAddresses',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowedReplicationHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getAllowedReplicationIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationIpAddresses',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowedReplicationSubnets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationSubnets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowedReplicationVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationVirtualGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getAllowedSubnets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowedSubnets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowedVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowedVirtualGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getBillingItemCategory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Category':

        data = self.client.call(
            self.service,
            'getBillingItemCategory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getBytesUsed(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBytesUsed',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCreationScheduleId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCreationScheduleId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCredentials(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'getCredentials',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def getDailySchedule(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getDailySchedule',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getDependentDuplicate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDependentDuplicate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDependentDuplicates(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getDependentDuplicates',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getEvents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getEvents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getFailbackNotAllowed(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFailbackNotAllowed',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFailoverNotAllowed(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFailoverNotAllowed',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFileNetworkMountAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFileNetworkMountAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFixReplicationCurrentStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFixReplicationCurrentStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHasEncryptionAtRest(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasEncryptionAtRest',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHourlySchedule(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getHourlySchedule',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getIntervalSchedule(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getIntervalSchedule',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getIops(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIops',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsConvertToIndependentTransactionInProgress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsConvertToIndependentTransactionInProgress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsDependentDuplicateProvisionCompleted(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsDependentDuplicateProvisionCompleted',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsInDedicatedServiceResource(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsInDedicatedServiceResource',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsMagneticStorage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIsMagneticStorage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsProvisionInProgress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsProvisionInProgress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsReadyForSnapshot(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsReadyForSnapshot',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsReadyToMount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsReadyToMount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIscsiLuns(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getIscsiLuns',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getIscsiReplicatingVolume(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getIscsiReplicatingVolume',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getIscsiTargetIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getIscsiTargetIpAddresses',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        
        return data


    def getLunId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getLunId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getManualSnapshots(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getManualSnapshots',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getMetricTrackingObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getMountPath(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMountPath',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMountableFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMountableFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMoveAndSplitStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMoveAndSplitStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNotificationSubscribers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getNotificationSubscribers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getOriginalSnapshotName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalSnapshotName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getOriginalVolumeId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalVolumeName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeSize(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalVolumeSize',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOsType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Iscsi_OS_Type':

        data = self.client.call(
            self.service,
            'getOsType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Iscsi.OS.Type import Type
        return Type(data)


    def getOsTypeId(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOsTypeId',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getParentPartnerships(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Partnership]':

        data = self.client.call(
            self.service,
            'getParentPartnerships',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Partnership import Partnership
        return Partnership(data)


    def getParentVolume(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getParentVolume',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getPartnerships(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Partnership]':

        data = self.client.call(
            self.service,
            'getPartnerships',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Partnership import Partnership
        return Partnership(data)


    def getPermissionsGroups(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getPermissionsGroups',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getProperties(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Property]':

        data = self.client.call(
            self.service,
            'getProperties',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Property import Property
        return Property(data)


    def getProvisionedIops(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getProvisionedIops',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReplicatingLuns(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getReplicatingLuns',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicatingVolume(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getReplicatingVolume',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicationEvents(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getReplicationEvents',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getReplicationPartners(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getReplicationPartners',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicationSchedule(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getReplicationSchedule',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getReplicationStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReplicationStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSchedules(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Schedule]':

        data = self.client.call(
            self.service,
            'getSchedules',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getServiceResource(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getServiceResource',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getServiceResourceBackendIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServiceResourceBackendIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getServiceResourceName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServiceResourceName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotCapacityGb(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotCapacityGb',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotCreationTimestamp(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotCreationTimestamp',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotDeletionThresholdPercentage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotDeletionThresholdPercentage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotNotificationStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotNotificationStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotSizeBytes(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotSizeBytes',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotSpaceAvailable(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotSpaceAvailable',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshots(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getSnapshots',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getStaasVersion(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getStaasVersion',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getStorageGroups(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getStorageGroups',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getStorageTierLevel(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getStorageTierLevel',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getStorageType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Type':

        data = self.client.call(
            self.service,
            'getStorageType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Type import Type
        return Type(data)


    def getTotalBytesUsed(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTotalBytesUsed',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalScheduleSnapshotRetentionCount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getTotalScheduleSnapshotRetentionCount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getUsageNotification(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification':

        data = self.client.call(
            self.service,
            'getUsageNotification',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification import Notification
        return Notification(data)


    def getVendorName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVendorName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualGuest(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVolumeHistory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_History]':

        data = self.client.call(
            self.service,
            'getVolumeHistory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.History import History
        return History(data)


    def getVolumeStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVolumeStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getWebccAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Password':

        data = self.client.call(
            self.service,
            'getWebccAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Password import Password
        return Password(data)


    def getWeeklySchedule(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getWeeklySchedule',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


