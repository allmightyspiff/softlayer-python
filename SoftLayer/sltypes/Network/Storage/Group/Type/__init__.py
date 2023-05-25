from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Group_Type(Entity):
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Group_Type'

    def getAllObjects(self) -> list['Network_Storage_Group_Type']:
        """Returns all storage group types available"""
        data = self.client.call('SoftLayer_Network_Storage_Group_Type', 'getAllObjects')
        from SoftLayer.sltypes.Network_Storage_Group_Type import Network_Storage_Group_Type
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Group_Type':
        """Retrieve a SoftLayer_Network_Storage_Group_Type record."""
        data = self.client.call('SoftLayer_Network_Storage_Group_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group_Type import Network_Storage_Group_Type
        return data
