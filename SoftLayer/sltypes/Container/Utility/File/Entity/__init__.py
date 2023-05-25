from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Utility_File_Entity(Entity):
    """SoftLayer_Container_Utility_File_Entity data type models a single entity on a storage resource. Entities can
include anything within a storage volume including files, folders, directories, and CloudLayer storage
projects."""
    content: str
    contentType: str
    createDate: datetime
    deleteDate: datetime
    id_: str
    isShared: int
    modifyDate: datetime
    name: str
    owner: str
    size: int
    type_: str
    version: int
