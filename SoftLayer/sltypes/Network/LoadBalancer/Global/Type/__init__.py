from SoftLayer.sltypes.Entity import Entity

class Network_LoadBalancer_Global_Type(Entity):
    """The global load balancer service has been deprecated and is no longer available.   The
SoftLayer_Network_LoadBalancer_Global_Type data type represents a single load balance method that can be
assigned to a global load balancer account. The load balance method determines how hosts in a load balancing
pool are chosen by the global load balancers."""
    id_: int
    name: str
