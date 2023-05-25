from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_LoadBalancerServerInstanceInfo(Entity):
    """SoftLayer_Network_LBaaS_LoadBalancerServerInstanceInfo specifies the application server, usually an IBM
SoftLayer virtual server or bare metal system, to be assigned to a load balancer."""
    privateIpAddress: str
    publicIpAddress: str
    weight: int
