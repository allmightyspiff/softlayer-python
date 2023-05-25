from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Attribute(Entity):
    """The SoftLayer_Hardware_Component_Attribute data type contains general information relating to a single
hardware setting or attribute for a component model. For Example: A RAID controller may be setup for many
different RAID configurations.  A RAID controller with a configuration of RAID-1 will have a single attribute
for this RAID setting."""
    hardwareComponentAttributeTypeId: int
    hardwareComponentId: int
    value: str
