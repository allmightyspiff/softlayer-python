from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Firmware_Attribute(Entity):
    """The SoftLayer_Hardware_Component_Firmware_Attribute data type contains general information for a hardware
model's firmware."""
    firmwareId: int
    id_: int
    typeId: int
    value: str
