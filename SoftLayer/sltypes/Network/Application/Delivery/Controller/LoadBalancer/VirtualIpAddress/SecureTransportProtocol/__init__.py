from SoftLayer.sltypes.Entity import Entity

class Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportProtocol(Entity):
    """Links a SSL transport protocol with a virtual IP address instance. Instances of this class are immutable and
should reflect a protocol that is configurable on a load balancer device."""
    id_: int
    keyName: str
    virtualIpAddressId: int
