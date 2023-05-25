from SoftLayer.sltypes.Network.Storage.Group import Network_Storage_Group
from SoftLayer.sltypes.Network_Storage_Group import Network_Storage_Group
from SoftLayer import BaseClient

class Network_Storage_Group_Iscsi(Network_Storage_Group):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Group_Iscsi'

    def addAllowedHost(self, identifier: int, allowedHost: 'Network_Storage_Allowed_Host') -> bool:
        """Attach a SoftLayer_Network_Storage_Allowed_Host object to this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group_Iscsi', 'addAllowedHost', allowedHost, id=identifier)
        return data

    def attachToVolume(self, identifier: int, volume: 'Network_Storage') -> bool:
        """Attach a SoftLayer_Network_Storage volume to this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group_Iscsi', 'attachToVolume', volume, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Group_Iscsi':
        """Retrieve a SoftLayer_Network_Storage_Group_Iscsi record."""
        data = self.client.call('SoftLayer_Network_Storage_Group_Iscsi', 'getObject', id=identifier)
        return data

    def removeAllowedHost(self, identifier: int, allowedHost: 'Network_Storage_Allowed_Host') -> bool:
        """Remove a SoftLayer_Network_Storage_Allowed_Host object from this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group_Iscsi', 'removeAllowedHost', allowedHost, id=identifier)
        return data

    def removeFromVolume(self, identifier: int, volume: 'Network_Storage') -> bool:
        """Remove a SoftLayer_Network_Storage volume from this group"""
        data = self.client.call('SoftLayer_Network_Storage_Group_Iscsi', 'removeFromVolume', volume, id=identifier)
        return data
