from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Model_Attribute_Type(Entity):
    """The SoftLayer_Hardware_Component_Model_Attribute_Type data type contains general information for the type of
an attribute for a hardware component model."""
    description: str
    id_: int
    keyName: str
    name: str
