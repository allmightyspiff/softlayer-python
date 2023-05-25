from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Model_Generic(Entity):
    """The SoftLayer_Hardware_Component_Model_Generic data type contains general information relating to a single
SoftLayer generic component model.  A generic component model represents a non-vendor specific representation
of a hardware component.  Frequently SoftLayer utilizes components from various vendors in the servers they
provision. For Example: Several different vendors produce 6GB DDR2 memory.  The generic component model for
the 6GB stick of RAM encompasses every instance of this component regardless of make and model."""
    capacity: float
    description: str
    hardwareComponentTypeId: int
    id_: int
    units: str
    upgradePriority: int
