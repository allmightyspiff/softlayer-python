from SoftLayer.sltypes.Entity import Entity

class Virtual_Disk_Image_Software(Entity):
    """A SoftLayer_Virtual_Disk_Image_Software record connects a computing instance's virtual disk images with
software records. This can be useful if a disk image is directly associated with software such as operating
systems."""
    id_: int
    softwareDescriptionId: int
