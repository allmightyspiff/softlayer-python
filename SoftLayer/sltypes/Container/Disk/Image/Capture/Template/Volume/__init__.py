from SoftLayer.sltypes.Container.Disk.Image.Capture.Template.Volume.Partition import Container_Disk_Image_Capture_Template_Volume_Partition
from SoftLayer.sltypes.Entity import Entity

class Container_Disk_Image_Capture_Template_Volume(Entity):
    bootVolumeFlag: bool
    name: str
    partitions: list[Container_Disk_Image_Capture_Template_Volume_Partition]
    storageGroupId: int
