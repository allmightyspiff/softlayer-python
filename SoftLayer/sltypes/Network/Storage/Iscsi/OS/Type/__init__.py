from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Iscsi_OS_Type(Entity):
    createDate: datetime
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Iscsi_OS_Type'

    def getAllObjects(self) -> list['Network_Storage_Iscsi_OS_Type']:
        """Returns all iSCSI OS Types"""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi_OS_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Iscsi_OS_Type':
        """Retrieve a SoftLayer_Network_Storage_Iscsi_OS_Type record."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi_OS_Type', 'getObject', id=identifier)
        return data
