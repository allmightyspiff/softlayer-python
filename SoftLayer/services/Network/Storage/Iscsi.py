# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Iscsi(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Iscsi'
        self.client = client

    def allowAccessFromHardware(
        self,
        hardwareObjectTemplate: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromHardware',
            hardwareObjectTemplate
        )
        
        return data


    def allowAccessFromIpAddress(
        self,
        ipAddressObjectTemplate: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromIpAddress',
            ipAddressObjectTemplate
        )
        
        return data


    def allowAccessFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromVirtualGuest',
            virtualGuestObjectTemplate
        )
        
        return data


    def allowAccessToReplicantFromHardwareList(
        self,
        hardwareObjectTemplates: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromHardwareList',
            hardwareObjectTemplates
        )
        
        return data


    def allowAccessToReplicantFromIpAddressList(
        self,
        ipAddressObjectTemplates: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromIpAddressList',
            ipAddressObjectTemplates
        )
        
        return data


    def allowAccessToReplicantFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromVirtualGuestList',
            virtualGuestObjectTemplates
        )
        
        return data


    def createOrUpdateLunId(
        self,
        lunId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Property':

        data = self.client.call(
            self.service,
            'createOrUpdateLunId',
            lunId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Property import Property
        return Property(data)


    def getMaximumExpansionSize(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getMaximumExpansionSize',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Iscsi':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Iscsi import Iscsi
        return Iscsi(data)


    def getSnapshotsForVolume(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getSnapshotsForVolume',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def removeAccessFromHardware(
        self,
        hardwareObjectTemplate: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromHardware',
            hardwareObjectTemplate
        )
        
        return data


    def removeAccessFromIpAddress(
        self,
        ipAddressObjectTemplate: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromIpAddress',
            ipAddressObjectTemplate
        )
        
        return data


    def removeAccessFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromVirtualGuest',
            virtualGuestObjectTemplate
        )
        
        return data


    def removeAccessToReplicantFromHardwareList(
        self,
        hardwareObjectTemplates: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromHardwareList',
            hardwareObjectTemplates
        )
        
        return data


    def removeAccessToReplicantFromIpAddressList(
        self,
        ipAddressObjectTemplates: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromIpAddressList',
            ipAddressObjectTemplates
        )
        
        return data


    def removeAccessToReplicantFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromVirtualGuestList',
            virtualGuestObjectTemplates
        )
        
        return data


    def allowAccessFromHardwareList(
        self,
        hardwareObjectTemplates: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromHardwareList',
            hardwareObjectTemplates
        )
        
        return data


    def allowAccessFromHost(
        self,
        typeClassName: str,
        hostId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'allowAccessFromHost',
            typeClassName,
            hostId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def allowAccessFromHostList(
        self,
        hostObjectTemplates: SoftLayer_Container_Network_Storage_Host,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'allowAccessFromHostList',
            hostObjectTemplates,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def allowAccessFromIpAddressList(
        self,
        ipAddressObjectTemplates: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromIpAddressList',
            ipAddressObjectTemplates
        )
        
        return data


    def allowAccessFromSubnet(
        self,
        subnetObjectTemplate: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromSubnet',
            subnetObjectTemplate
        )
        
        return data


    def allowAccessFromSubnetList(
        self,
        subnetObjectTemplates: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromSubnetList',
            subnetObjectTemplates
        )
        
        return data


    def allowAccessFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessFromVirtualGuestList',
            virtualGuestObjectTemplates
        )
        
        return data


    def allowAccessToReplicantFromHardware(
        self,
        hardwareObjectTemplate: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromHardware',
            hardwareObjectTemplate
        )
        
        return data


    def allowAccessToReplicantFromIpAddress(
        self,
        ipAddressObjectTemplate: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromIpAddress',
            ipAddressObjectTemplate
        )
        
        return data


    def allowAccessToReplicantFromSubnet(
        self,
        subnetObjectTemplate: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromSubnet',
            subnetObjectTemplate
        )
        
        return data


    def allowAccessToReplicantFromSubnetList(
        self,
        subnetObjectTemplates: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromSubnetList',
            subnetObjectTemplates
        )
        
        return data


    def allowAccessToReplicantFromVirtualGuest(
        self,
        virtualGuestObjectTemplate: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'allowAccessToReplicantFromVirtualGuest',
            virtualGuestObjectTemplate
        )
        
        return data


    def assignCredential(
        self,
        username: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'assignCredential',
            username
        )
        
        return data


    def assignNewCredential(
        self,
        type: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Credential':

        data = self.client.call(
            self.service,
            'assignNewCredential',
            type,
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
        startDate: dateTime,
        endDate: dateTime
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'collectBandwidth',
            type,
            startDate,
            endDate
        )
        
        return data


    def collectBytesUsed(
        self,
        
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'collectBytesUsed',
            
        )
        
        return data


    def convertCloneDependentToIndependent(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'convertCloneDependentToIndependent',
            
        )
        
        return data


    def createFolder(
        self,
        folder: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createFolder',
            folder
        )
        
        return data


    def createSnapshot(
        self,
        notes: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'createSnapshot',
            notes,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def deleteAllFiles(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteAllFiles',
            
        )
        
        return data


    def deleteFile(
        self,
        fileId: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFile',
            fileId
        )
        
        return data


    def deleteFiles(
        self,
        fileIds: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFiles',
            fileIds
        )
        
        return data


    def deleteFolder(
        self,
        folder: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteFolder',
            folder
        )
        
        return data


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def disableSnapshots(
        self,
        scheduleType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disableSnapshots',
            scheduleType
        )
        
        return data


    def disasterRecoveryFailoverToReplicant(
        self,
        replicantId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disasterRecoveryFailoverToReplicant',
            replicantId
        )
        
        return data


    def downloadFile(
        self,
        fileId: str
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'downloadFile',
            fileId
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def editCredential(
        self,
        username: str,
        newPassword: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editCredential',
            username,
            newPassword
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def enableSnapshots(
        self,
        scheduleType: str,
        retentionCount: int,
        minute: int,
        hour: int,
        dayOfWeek: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enableSnapshots',
            scheduleType,
            retentionCount,
            minute,
            hour,
            dayOfWeek
        )
        
        return data


    def failbackFromReplicant(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'failbackFromReplicant',
            
        )
        
        return data


    def failoverToReplicant(
        self,
        replicantId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'failoverToReplicant',
            replicantId
        )
        
        return data


    def getAllFiles(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getAllFiles',
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getAllFilesByFilter(
        self,
        filter: SoftLayer_Container_Utility_File_Entity,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getAllFilesByFilter',
            filter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getAllowableHardware(
        self,
        filterHostname: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowableHardware',
            filterHostname,
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
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowableIpAddresses',
            subnetId,
            filterIpAddress,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowableSubnets(
        self,
        filterNetworkIdentifier: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowableSubnets',
            filterNetworkIdentifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowableVirtualGuests(
        self,
        filterHostname: str,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowableVirtualGuests',
            filterHostname,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getAllowedHostsLimit(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAllowedHostsLimit',
            
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
        
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_ContentDeliveryUrl]':

        data = self.client.call(
            self.service,
            'getCdnUrls',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.ContentDeliveryUrl import ContentDeliveryUrl
        return ContentDeliveryUrl(data)


    def getClusterResource(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getClusterResource',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getDuplicateConversionStatus(
        self,
        
    ) -> 'SoftLayer_Container_Network_Storage_DuplicateConversionStatusInformation':

        data = self.client.call(
            self.service,
            'getDuplicateConversionStatus',
            
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
        identifier: str
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'getFileByIdentifier',
            identifier
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFileCount(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getFileCount',
            
        )
        
        return data


    def getFileList(
        self,
        folder: str,
        path: str
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getFileList',
            folder,
            path
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFilePendingDeleteCount(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getFilePendingDeleteCount',
            
        )
        
        return data


    def getFilesPendingDelete(
        self,
        
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':

        data = self.client.call(
            self.service,
            'getFilesPendingDelete',
            
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getFolderList(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Folder]':

        data = self.client.call(
            self.service,
            'getFolderList',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Folder import Folder
        return Folder(data)


    def getGraph(
        self,
        startDate: dateTime,
        endDate: dateTime,
        type: str
    ) -> 'SoftLayer_Container_Bandwidth_GraphOutputs':

        data = self.client.call(
            self.service,
            'getGraph',
            startDate,
            endDate,
            type
        )
        from SoftLayer.datatypes.Container.Bandwidth.GraphOutputs import GraphOutputs
        return GraphOutputs(data)


    def getNetworkConnectionDetails(
        self,
        
    ) -> 'SoftLayer_Container_Network_Storage_NetworkConnectionInformation':

        data = self.client.call(
            self.service,
            'getNetworkConnectionDetails',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


    def getNetworkMountAddress(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNetworkMountAddress',
            
        )
        
        return data


    def getNetworkMountPath(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNetworkMountPath',
            
        )
        
        return data


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
        credentialObject: SoftLayer_Network_Storage_Credential,
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
        fileId: str
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'getRecycleBinFileByIdentifier',
            fileId
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def getRemainingAllowedHosts(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getRemainingAllowedHosts',
            
        )
        
        return data


    def getRemainingAllowedHostsForReplicant(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getRemainingAllowedHostsForReplicant',
            
        )
        
        return data


    def getReplicationTimestamp(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReplicationTimestamp',
            
        )
        
        return data


    def getStorageGroupsNetworkConnectionDetails(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Storage_NetworkConnectionInformation]':

        data = self.client.call(
            self.service,
            'getStorageGroupsNetworkConnectionDetails',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


    def getTargetIpAddresses(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getTargetIpAddresses',
            
        )
        
        return data


    def getValidReplicationTargetDatacenterLocations(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getValidReplicationTargetDatacenterLocations',
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
        
    ) -> 'SoftLayer_Container_Network_Storage_VolumeDuplicateParameters':

        data = self.client.call(
            self.service,
            'getVolumeDuplicateParameters',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.VolumeDuplicateParameters import VolumeDuplicateParameters
        return VolumeDuplicateParameters(data)


    def immediateFailoverToReplicant(
        self,
        replicantId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'immediateFailoverToReplicant',
            replicantId
        )
        
        return data


    def initiateOriginVolumeReclaim(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'initiateOriginVolumeReclaim',
            
        )
        
        return data


    def initiateVolumeCutover(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'initiateVolumeCutover',
            
        )
        
        return data


    def isBlockingOperationInProgress(
        self,
        exemptStatusKeyNames: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isBlockingOperationInProgress',
            exemptStatusKeyNames
        )
        
        return data


    def isDuplicateReadyForSnapshot(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isDuplicateReadyForSnapshot',
            
        )
        
        return data


    def isDuplicateReadyToMount(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isDuplicateReadyToMount',
            
        )
        
        return data


    def isVolumeActive(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isVolumeActive',
            
        )
        
        return data


    def refreshDependentDuplicate(
        self,
        snapshotId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshDependentDuplicate',
            snapshotId
        )
        
        return data


    def refreshDuplicate(
        self,
        snapshotId: int,
        forceRefresh: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshDuplicate',
            snapshotId,
            forceRefresh
        )
        
        return data


    def removeAccessFromHardwareList(
        self,
        hardwareObjectTemplates: SoftLayer_Hardware
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromHardwareList',
            hardwareObjectTemplates
        )
        
        return data


    def removeAccessFromHost(
        self,
        typeClassName: str,
        hostId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Storage_Allowed_Host':

        data = self.client.call(
            self.service,
            'removeAccessFromHost',
            typeClassName,
            hostId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def removeAccessFromHostList(
        self,
        hostObjectTemplates: SoftLayer_Container_Network_Storage_Host,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'removeAccessFromHostList',
            hostObjectTemplates,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def removeAccessFromIpAddressList(
        self,
        ipAddressObjectTemplates: SoftLayer_Network_Subnet_IpAddress
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromIpAddressList',
            ipAddressObjectTemplates
        )
        
        return data


    def removeAccessFromSubnet(
        self,
        subnetObjectTemplate: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromSubnet',
            subnetObjectTemplate
        )
        
        return data


    def removeAccessFromSubnetList(
        self,
        subnetObjectTemplates: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromSubnetList',
            subnetObjectTemplates
        )
        
        return data


    def removeAccessFromVirtualGuestList(
        self,
        virtualGuestObjectTemplates: SoftLayer_Virtual_Guest
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessFromVirtualGuestList',
            virtualGuestObjectTemplates
        )
        
        return data


    def removeAccessToReplicantFromSubnet(
        self,
        subnetObjectTemplate: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromSubnet',
            subnetObjectTemplate
        )
        
        return data


    def removeAccessToReplicantFromSubnetList(
        self,
        subnetObjectTemplates: SoftLayer_Network_Subnet
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAccessToReplicantFromSubnetList',
            subnetObjectTemplates
        )
        
        return data


    def removeCredential(
        self,
        username: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeCredential',
            username
        )
        
        return data


    def restoreFile(
        self,
        fileId: str
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'restoreFile',
            fileId
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def restoreFromSnapshot(
        self,
        snapshotId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'restoreFromSnapshot',
            snapshotId
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
        mountable: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setMountable',
            mountable
        )
        
        return data


    def setSnapshotAllocation(
        self,
        capacityGb: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setSnapshotAllocation',
            capacityGb
        )
        
        return data


    def setSnapshotNotification(
        self,
        notificationFlag: boolean
    ) -> 'void':

        data = self.client.call(
            self.service,
            'setSnapshotNotification',
            notificationFlag
        )
        
        return data


    def upgradeVolumeCapacity(
        self,
        itemId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'upgradeVolumeCapacity',
            itemId
        )
        
        return data


    def uploadFile(
        self,
        file: SoftLayer_Container_Utility_File_Entity
    ) -> 'SoftLayer_Container_Utility_File_Entity':

        data = self.client.call(
            self.service,
            'uploadFile',
            file
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return Entity(data)


    def validateHostsAccess(
        self,
        hostObjectTemplates: SoftLayer_Container_Network_Storage_Host
    ) -> 'list[SoftLayer_Container_Network_Storage_HostsGatewayInformation]':

        data = self.client.call(
            self.service,
            'validateHostsAccess',
            hostObjectTemplates
        )
        from SoftLayer.datatypes.Container.Network.Storage.HostsGatewayInformation import HostsGatewayInformation
        return HostsGatewayInformation(data)


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


    def getAccountPassword(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Password':

        data = self.client.call(
            self.service,
            'getAccountPassword',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Password import Password
        return Password(data)


    def getActiveTransactions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':

        data = self.client.call(
            self.service,
            'getActiveTransactions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return Transaction(data)


    def getAllowDisasterRecoveryFailback(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAllowDisasterRecoveryFailback',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllowDisasterRecoveryFailover(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAllowDisasterRecoveryFailover',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllowedHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowedHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getAllowedIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowedIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowedReplicationHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getAllowedReplicationIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getAllowedReplicationSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowedReplicationVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowedReplicationVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getAllowedSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getAllowedSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getAllowedVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getAllowedVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getBillingItemCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Category':

        data = self.client.call(
            self.service,
            'getBillingItemCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getBytesUsed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBytesUsed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCreationScheduleId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCreationScheduleId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCredentials(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Credential]':

        data = self.client.call(
            self.service,
            'getCredentials',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Credential import Credential
        return Credential(data)


    def getDailySchedule(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getDailySchedule',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getDependentDuplicate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDependentDuplicate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDependentDuplicates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getDependentDuplicates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getFailbackNotAllowed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFailbackNotAllowed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFailoverNotAllowed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFailoverNotAllowed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFileNetworkMountAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFileNetworkMountAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFixReplicationCurrentStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getFixReplicationCurrentStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHasEncryptionAtRest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasEncryptionAtRest',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHourlySchedule(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getHourlySchedule',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getIntervalSchedule(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getIntervalSchedule',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getIops(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIops',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsConvertToIndependentTransactionInProgress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsConvertToIndependentTransactionInProgress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsDependentDuplicateProvisionCompleted(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsDependentDuplicateProvisionCompleted',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsInDedicatedServiceResource(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsInDedicatedServiceResource',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsMagneticStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIsMagneticStorage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsProvisionInProgress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsProvisionInProgress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsReadyForSnapshot(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsReadyForSnapshot',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsReadyToMount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsReadyToMount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIscsiLuns(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getIscsiLuns',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getIscsiReplicatingVolume(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getIscsiReplicatingVolume',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getIscsiTargetIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getIscsiTargetIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        
        return data


    def getLunId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getLunId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getManualSnapshots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getManualSnapshots',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getMetricTrackingObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getMountPath(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMountPath',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMountableFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMountableFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMoveAndSplitStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMoveAndSplitStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNotificationSubscribers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getNotificationSubscribers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getOriginalSnapshotName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalSnapshotName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getOriginalVolumeId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalVolumeName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOriginalVolumeSize(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOriginalVolumeSize',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOsType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Iscsi_OS_Type':

        data = self.client.call(
            self.service,
            'getOsType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Iscsi.OS.Type import Type
        return Type(data)


    def getOsTypeId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getOsTypeId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getParentPartnerships(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Partnership]':

        data = self.client.call(
            self.service,
            'getParentPartnerships',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Partnership import Partnership
        return Partnership(data)


    def getParentVolume(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getParentVolume',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getPartnerships(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Partnership]':

        data = self.client.call(
            self.service,
            'getPartnerships',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Partnership import Partnership
        return Partnership(data)


    def getPermissionsGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getPermissionsGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getProperties(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Property]':

        data = self.client.call(
            self.service,
            'getProperties',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Property import Property
        return Property(data)


    def getProvisionedIops(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getProvisionedIops',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReplicatingLuns(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getReplicatingLuns',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicatingVolume(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage':

        data = self.client.call(
            self.service,
            'getReplicatingVolume',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicationEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getReplicationEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getReplicationPartners(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getReplicationPartners',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getReplicationSchedule(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getReplicationSchedule',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getReplicationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getReplicationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSchedules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Schedule]':

        data = self.client.call(
            self.service,
            'getSchedules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


    def getServiceResource(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Resource':

        data = self.client.call(
            self.service,
            'getServiceResource',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Resource import Resource
        return Resource(data)


    def getServiceResourceBackendIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServiceResourceBackendIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getServiceResourceName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getServiceResourceName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotCapacityGb(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotCapacityGb',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotCreationTimestamp(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotCreationTimestamp',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotDeletionThresholdPercentage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotDeletionThresholdPercentage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotNotificationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotNotificationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotSizeBytes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotSizeBytes',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshotSpaceAvailable(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSnapshotSpaceAvailable',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSnapshots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getSnapshots',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getStaasVersion(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getStaasVersion',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getStorageGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getStorageGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getStorageTierLevel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getStorageTierLevel',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getStorageType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Type':

        data = self.client.call(
            self.service,
            'getStorageType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Type import Type
        return Type(data)


    def getTotalBytesUsed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTotalBytesUsed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalScheduleSnapshotRetentionCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getTotalScheduleSnapshotRetentionCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getUsageNotification(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification':

        data = self.client.call(
            self.service,
            'getUsageNotification',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification import Notification
        return Notification(data)


    def getVendorName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVendorName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVolumeHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_History]':

        data = self.client.call(
            self.service,
            'getVolumeHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.History import History
        return History(data)


    def getVolumeStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVolumeStatus',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getWebccAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Password':

        data = self.client.call(
            self.service,
            'getWebccAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Password import Password
        return Password(data)


    def getWeeklySchedule(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Schedule':

        data = self.client.call(
            self.service,
            'getWeeklySchedule',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Schedule import Schedule
        return Schedule(data)


