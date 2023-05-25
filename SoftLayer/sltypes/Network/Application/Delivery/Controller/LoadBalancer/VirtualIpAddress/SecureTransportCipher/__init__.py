from SoftLayer.sltypes.Entity import Entity

class Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress_SecureTransportCipher(Entity):
    """A single cipher configured for a load balancer virtual IP address instance. Instances of this class are
immutable and should reflect a cipher that is configurable on a load balancer device."""
    id_: int
    keyName: str
    virtualIpAddressId: int
