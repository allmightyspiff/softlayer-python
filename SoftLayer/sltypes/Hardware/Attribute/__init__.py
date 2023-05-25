from SoftLayer.sltypes.Entity import Entity

class Hardware_Attribute(Entity):
    """The SoftLayer_Hardware_Attribute type contains general information for a hardware attribute. Hardware
attributes can be assigned to specific hardware objects to describe relatively arbitrary information."""
    hardwareAttributeTypeId: int
    id_: int
    value: str
