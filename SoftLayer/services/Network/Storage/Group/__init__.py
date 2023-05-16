# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Group'
        self.client = client

    def addAllowedHost(
        self,
        allowedHost: 'SoftLayer_Network_Storage_Allowed_Host',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addAllowedHost',
            allowedHost,
            id=identifier
        )
        
        return data


    def attachToVolume(
        self,
        volume: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'attachToVolume',
            volume,
            id=identifier
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_Network_Storage_Group'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
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


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Storage_Group',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
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
        identifier: int
    ) -> 'SoftLayer_Container_Network_Storage_NetworkConnectionInformation':

        data = self.client.call(
            self.service,
            'getNetworkConnectionDetails',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return NetworkConnectionInformation(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Group':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def removeAllowedHost(
        self,
        allowedHost: 'SoftLayer_Network_Storage_Allowed_Host',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAllowedHost',
            allowedHost,
            id=identifier
        )
        
        return data


    def removeFromVolume(
        self,
        volume: 'SoftLayer_Network_Storage',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeFromVolume',
            volume,
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


    def getAllowedHosts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Allowed_Host]':

        data = self.client.call(
            self.service,
            'getAllowedHosts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Allowed.Host import Host
        return Host(data)


    def getAttachedVolumes(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getAttachedVolumes',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getGroupType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Group_Type':

        data = self.client.call(
            self.service,
            'getGroupType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Group.Type import Type
        return Type(data)


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


