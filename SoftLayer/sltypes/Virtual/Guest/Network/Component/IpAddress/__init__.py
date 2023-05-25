from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Network_Component_IpAddress(Entity):
    """The SoftLayer_Virtual_Guest_Network_Component_IpAddress data type contains general information relating to
the binding of a single network component to a single SoftLayer IP address."""
    ipAddressId: int
    port: int
    type_: str
