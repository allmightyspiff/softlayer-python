from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Group(Entity):
    accountId: int
    alias: str
    createDate: datetime
    groupTypeId: int
    id_: int
    modifyDate: datetime
    osTypeId: int
    serviceResourceId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Group'

    def addAllowedHost(self, identifier: int, allowedHost: 'Network_Storage_Allowed_Host') -> bool:
        """Attach a SoftLayer_Network_Storage_Allowed_Host object to this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'addAllowedHost', allowedHost, id=identifier)
        return data

    def attachToVolume(self, identifier: int, volume: 'Network_Storage') -> bool:
        """Attach a SoftLayer_Network_Storage volume to this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'attachToVolume', volume, id=identifier)
        return data

    def createObject(self, templateObject: 'Network_Storage_Group') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Group', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Group', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Storage_Group') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Group', 'editObject', templateObject, id=identifier)
        return data

    def getAllObjects(self) -> list['Network_Storage_Group']:
        """Returns all network storage groups"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getAllObjects')
        return data

    def getNetworkConnectionDetails(self, identifier: int) -> 'Container_Network_Storage_NetworkConnectionInformation':
        """Retrieve network connection information for SoftLayer_Network_Storage_Allowed_Host objects to connect to the
Network Storage Volumes within this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getNetworkConnectionDetails', id=identifier)
        from SoftLayer.sltypes.Container_Network_Storage_NetworkConnectionInformation import Container_Network_Storage_NetworkConnectionInformation
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Group':
        """Retrieve a SoftLayer_Network_Storage_Group record."""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getObject', id=identifier)
        return data

    def removeAllowedHost(self, identifier: int, allowedHost: 'Network_Storage_Allowed_Host') -> bool:
        """Remove a SoftLayer_Network_Storage_Allowed_Host object from this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'removeAllowedHost', allowedHost, id=identifier)
        return data

    def removeFromVolume(self, identifier: int, volume: 'Network_Storage') -> bool:
        """Remove a SoftLayer_Network_Storage volume from this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'removeFromVolume', volume, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAllowedHosts(self, identifier: int) -> list['Network_Storage_Allowed_Host']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getAllowedHosts', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
        return data

    def getAttachedVolumes(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getAttachedVolumes', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getGroupType(self, identifier: int) -> 'Network_Storage_Group_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getGroupType', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group_Type import Network_Storage_Group_Type
        return data

    def getOsType(self, identifier: int) -> 'Network_Storage_Iscsi_OS_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getOsType', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Iscsi_OS_Type import Network_Storage_Iscsi_OS_Type
        return data

    def getServiceResource(self, identifier: int) -> 'Network_Service_Resource':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Group', 'getServiceResource', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data
