from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Model_Generic_Attribute(Entity):
    """The SoftLayer_Hardware_Component_Model_Generic_Attribute data type contains information relating to a single
SoftLayer generic component model.  Generic component model attributes can hold any information to describe
functionality of the model. For Example: The number of cores that a processor has."""
    value: str
