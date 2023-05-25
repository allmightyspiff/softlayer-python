from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_L7Member(Entity):
    """The SoftLayer_Network_LBaaS_L7Member represents the backend member for a L7 pool. It can be either a virtual
server or a bare metal machine."""
    address: str
    createDate: datetime
    id_: int
    modifyDate: datetime
    port: int
    provisioningStatus: str
    uuid: str
    weight: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_L7Member'

    def addL7PoolMembers(self, l7PoolUuid: str, memberInstances: 'Network_LBaaS_L7Member') -> 'Network_LBaaS_LoadBalancer':
        """Add load balancer L7 members"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Member', 'addL7PoolMembers', l7PoolUuid, memberInstances)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def deleteL7PoolMembers(self, l7PoolUuid: str, memberUuids: str) -> 'Network_LBaaS_LoadBalancer':
        """Delete load balancer members"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Member', 'deleteL7PoolMembers', l7PoolUuid, memberUuids)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_L7Member':
        """Retrieve a SoftLayer_Network_LBaaS_L7Member record."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Member', 'getObject', id=identifier)
        return data

    def updateL7PoolMembers(self, l7PoolUuid: str, members: 'Network_LBaaS_L7Member') -> 'Network_LBaaS_LoadBalancer':
        """Update l7 members weight and port"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Member', 'updateL7PoolMembers', l7PoolUuid, members)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data
