from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_L7Pool(Entity):
    """The SoftLayer_Network_LBaaS_L7Pool type presents a structure containing attributes of a load balancer's L7
pool such as the protocol, and the load balancing algorithm used. L7 pool is used for redirect_pool action of
the L7 policy and is different from the default pool"""
    createDate: datetime
    id_: int
    loadBalancingAlgorithm: str
    modifyDate: datetime
    name: str
    protocol: str
    provisioningStatus: str
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_L7Pool'

    def createL7Pool(self, loadBalancerUuid: str, l7Pool: 'Network_LBaaS_L7Pool', l7Members: 'Network_LBaaS_L7Member', l7HealthMonitor: 'Network_LBaaS_L7HealthMonitor', l7SessionAffinity: 'Network_LBaaS_L7SessionAffinity') -> 'Network_LBaaS_LoadBalancer':
        """create L7 pools"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'createL7Pool', loadBalancerUuid, l7Pool, l7Members, l7HealthMonitor, l7SessionAffinity)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def deleteObject(self, identifier: int) -> 'Network_LBaaS_LoadBalancer':
        """deletes L7 pools"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'deleteObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getL7PoolMemberHealth(self, loadBalancerUuid: str) -> list['Network_LBaaS_L7PoolMembersHealth']:
        """Return load balancer's all L7 pools members health"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getL7PoolMemberHealth', loadBalancerUuid)
        from SoftLayer.sltypes.Network_LBaaS_L7PoolMembersHealth import Network_LBaaS_L7PoolMembersHealth
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_L7Pool':
        """Retrieve a SoftLayer_Network_LBaaS_L7Pool record."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getObject', id=identifier)
        return data

    def updateL7Pool(self, l7PoolUuid: str, l7Pool: 'Network_LBaaS_L7Pool', l7HealthMonitor: 'Network_LBaaS_L7HealthMonitor', l7SessionAffinity: 'Network_LBaaS_L7SessionAffinity') -> 'Network_LBaaS_LoadBalancer':
        """updates L7 pools"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'updateL7Pool', l7PoolUuid, l7Pool, l7HealthMonitor, l7SessionAffinity)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getL7HealthMonitor(self, identifier: int) -> 'Network_LBaaS_L7HealthMonitor':
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getL7HealthMonitor', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7HealthMonitor import Network_LBaaS_L7HealthMonitor
        return data

    def getL7Members(self, identifier: int) -> list['Network_LBaaS_L7Member']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getL7Members', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Member import Network_LBaaS_L7Member
        return data

    def getL7Policies(self, identifier: int) -> list['Network_LBaaS_L7Policy']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getL7Policies', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Policy import Network_LBaaS_L7Policy
        return data

    def getL7SessionAffinity(self, identifier: int) -> 'Network_LBaaS_L7SessionAffinity':
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Pool', 'getL7SessionAffinity', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7SessionAffinity import Network_LBaaS_L7SessionAffinity
        return data
