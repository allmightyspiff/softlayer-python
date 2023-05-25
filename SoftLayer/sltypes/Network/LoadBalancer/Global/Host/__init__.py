from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LoadBalancer_Global_Host(Entity):
    """The global load balancer service has been deprecated and is no longer available."""
    destinationIp: str
    destinationPort: int
    enabled: int
    healthCheck: str
    hits: float
    id_: int
    loadBalanceOrder: int
    location: str
    status: str
    weight: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LoadBalancer_Global_Host'

    def deleteObject(self, identifier: int) -> bool:
        """[Deprecated] Remove a host from the load balancing pool of a global load balancer account."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Host', 'deleteObject', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_LoadBalancer_Global_Host':
        """Retrieve a SoftLayer_Network_LoadBalancer_Global_Host record."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Host', 'getObject', id=identifier)
        return data

    def getLoadBalancerAccount(self, identifier: int) -> 'Network_LoadBalancer_Global_Account':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Host', 'getLoadBalancerAccount', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Global_Account import Network_LoadBalancer_Global_Account
        return data
