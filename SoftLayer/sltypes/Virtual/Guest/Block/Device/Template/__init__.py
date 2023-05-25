from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Block_Device_Template(Entity):
    """The virtual block device template data type presents the structure in which all archived image templates are
presented.   A virtual block device template, also known as a image template, represents the image of a
virtual guest instance."""
    device: str
    diskImageId: int
    diskSpace: float
    groupId: int
    id_: int
    units: str
