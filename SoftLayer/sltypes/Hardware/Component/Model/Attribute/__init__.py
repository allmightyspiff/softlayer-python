from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Model_Attribute(Entity):
    """The SoftLayer_Hardware_Component__Model_Attribute data type contains general information relating to a single
hardware setting or attribute for a component model."""
    attributeTypeId: int
    hardwareComponentModelId: int
    value: str
