from SoftLayer.sltypes.Container.Image.StorageGroupDetails.Drives import Container_Image_StorageGroupDetails_Drives
from SoftLayer.sltypes.Entity import Entity

class Container_Image_StorageGroupDetails(Entity):
    drives: list[Container_Image_StorageGroupDetails_Drives]
    storageGroupName: str
    storageGroupType: str
