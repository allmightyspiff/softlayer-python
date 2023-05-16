# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Group'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkConnectionDetails(
        self,
        
    ) -> 'SoftLayer_Container_Network_Storage_NetworkConnectionInformation':
        data = self.client.call(
            self.service,
            'getNetworkConnectionDetails',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.NetworkConnectionInformation import NetworkConnectionInformation
        return SL_NetworkConnectionInformation(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Group':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Storage(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Resource(data)


