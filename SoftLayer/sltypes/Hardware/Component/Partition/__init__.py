from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Partition(Entity):
    """The SoftLayer_Hardware_Component_Partition data type contains general information relating to a single hard
drive partition."""
    diskNumber: int
    grow: int
    hardwareComponentId: int
    minimumSize: float
    name: str
