from SoftLayer.sltypes.Entity import Entity

class Virtual_Disk_Image_Type(Entity):
    """SoftLayer_Virtual_Disk_Image_Type models the types of virtual disk images available to CloudLayer Computing
Instances. Virtual disk image types describe if an image's data is preservable when upgraded, whether a disk
contains a suspended virtual image, or if a disk contains crash dump information."""
    description: str
    keyName: str
    name: str
