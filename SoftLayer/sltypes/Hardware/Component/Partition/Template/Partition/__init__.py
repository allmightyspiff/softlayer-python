from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Partition_Template_Partition(Entity):
    """The SoftLayer_Hardware_Component_Partition_Template_Partition data type contains general information relating
to a single SoftLayer Template Partition."""
    id_: int
    isGrow: bool
    partitionName: str
    partitionSize: float
    partitionTemplateId: int
    volumeNumber: int
