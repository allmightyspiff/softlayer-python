from SoftLayer.sltypes.Entity import Entity

class Container_Utility_Network_Subnet_Mask_Generic_Detail(Entity):
    """The SoftLayer_Container_Utility_Network_Subnet_Mask_Generic_Detail data type contains information relating to
a subnet mask and details associated with that object."""
    cidr: str
    description: str
    mask: str
