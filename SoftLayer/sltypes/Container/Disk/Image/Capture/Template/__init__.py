from SoftLayer.sltypes.Container.Disk.Image.Capture.Template.Volume import Container_Disk_Image_Capture_Template_Volume
from SoftLayer.sltypes.Entity import Entity

class Container_Disk_Image_Capture_Template(Entity):
    description: str
    name: str
    summary: str
    volumes: list[Container_Disk_Image_Capture_Template_Volume]
