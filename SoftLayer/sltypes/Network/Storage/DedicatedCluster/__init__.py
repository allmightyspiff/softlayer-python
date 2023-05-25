from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_DedicatedCluster(Entity):
    accountId: int
    createDate: datetime
    id_: int
    serviceResourceId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_DedicatedCluster'

    def getDedicatedClusterList(self) -> list[int]:
        data = self.client.call('SoftLayer_Network_Storage_DedicatedCluster', 'getDedicatedClusterList')
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_DedicatedCluster':
        """Retrieve a SoftLayer_Network_Storage_DedicatedCluster record."""
        data = self.client.call('SoftLayer_Network_Storage_DedicatedCluster', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_DedicatedCluster', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getServiceResource(self, identifier: int) -> 'Network_Service_Resource':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_DedicatedCluster', 'getServiceResource', id=identifier)
        from SoftLayer.sltypes.Network_Service_Resource import Network_Service_Resource
        return data
