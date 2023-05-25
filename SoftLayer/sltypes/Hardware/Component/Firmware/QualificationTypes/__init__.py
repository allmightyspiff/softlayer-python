from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Firmware_QualificationTypes(Entity):
    """The SoftLayer_Hardware_Component_Firmware_QualificationTypes data type describes the current qualification
status for a particular firmware."""
    description: str
    id_: int
    keyName: str
    name: str
