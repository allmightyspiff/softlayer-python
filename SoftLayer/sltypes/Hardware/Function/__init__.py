from SoftLayer.sltypes.Entity import Entity

class Hardware_Function(Entity):
    """The SoftLayer_Hardware_Function data type contains a generic object type for a piece of hardware, like
switch, firewall, server, etc.."""
    code: str
    description: str
    id_: int
