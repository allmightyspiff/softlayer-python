# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Group_Iscsi(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Group_Iscsi'
        self.client = client

    def addAllowedHost(
        self,
        allowedHost: SoftLayer_Network_Storage_Allowed_Host
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addAllowedHost',
            allowedHost
        )
        
        return data


    def attachToVolume(
        self,
        volume: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'attachToVolume',
            volume
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Group_Iscsi':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Group.Iscsi import Iscsi
        return Iscsi(data)


    def removeAllowedHost(
        self,
        allowedHost: SoftLayer_Network_Storage_Allowed_Host
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllowedHost',
            allowedHost
        )
        
        return data


    def removeFromVolume(
        self,
        volume: SoftLayer_Network_Storage
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeFromVolume',
            volume
        )
        
        return data


    def createObject(
        self,
        templateObject: SoftLayer_Network_Storage_Group
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
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


    def editObject(
        self,
        templateObject: SoftLayer_Network_Storage_Group
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getNetworkConnectionDetails(
        self,
        
    ) -> 'SoftLayer_Container_Network_Storage_NetworkConnectionInformation':

        data = self.client.call(
            self.service,
            'getNetworkConnectionDetails',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


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


    def getAllowedHosts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'getAllowedHosts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def getAttachedVolumes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAttachedVolumes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getGroupType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Group_Type':

        data = self.client.call(
            self.service,
            'getGroupType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Group.Type import Type
        return Type(data)


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


