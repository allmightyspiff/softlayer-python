from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_Member(Entity):
    """The SoftLayer_Network_LBaaS_Member represents the backend member for a load balancer. It can be either a
virtual server or a bare metal machine."""
    address: str
    createDate: datetime
    id_: int
    modifyDate: datetime
    provisioningStatus: str
    uuid: str
    weight: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_Member'

    def addLoadBalancerMembers(self, loadBalancerUuid: str, serverInstances: 'Network_LBaaS_LoadBalancerServerInstanceInfo') -> 'Network_LBaaS_LoadBalancer':
        """Add load balancer members"""
        data = self.client.call('SoftLayer_Network_LBaaS_Member', 'addLoadBalancerMembers', loadBalancerUuid, serverInstances)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def deleteLoadBalancerMembers(self, loadBalancerUuid: str, memberUuids: str) -> 'Network_LBaaS_LoadBalancer':
        """Delete load balancer members"""
        data = self.client.call('SoftLayer_Network_LBaaS_Member', 'deleteLoadBalancerMembers', loadBalancerUuid, memberUuids)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_Member':
        """Retrieve a SoftLayer_Network_LBaaS_Member record."""
        data = self.client.call('SoftLayer_Network_LBaaS_Member', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_Member import Network_LBaaS_Member
        return data

    def updateLoadBalancerMembers(self, loadBalancerUuid: str, members: 'Network_LBaaS_Member') -> 'Network_LBaaS_LoadBalancer':
        """Update members weight"""
        data = self.client.call('SoftLayer_Network_LBaaS_Member', 'updateLoadBalancerMembers', loadBalancerUuid, members)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data
