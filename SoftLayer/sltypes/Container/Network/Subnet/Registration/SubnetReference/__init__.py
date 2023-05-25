from SoftLayer.sltypes.Entity import Entity

class Container_Network_Subnet_Registration_SubnetReference(Entity):
    """SoftLayer_Container_Network_Subnet_Registration_SubnetReference is provided to reference
[[SoftLayer_Network_Subnet_Registration]] object and the [[SoftLayer_Network_Subnet]] it references, in CIDR
form."""
    registrationId: int
    subnetCidr: str
