from SoftLayer.sltypes.Container.Utility.File.Entity import Container_Utility_File_Entity
from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity

class Container_Network_Storage_Hub_ObjectStorage_File(Container_Utility_File_Entity):
    """SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File provides specific details that only apply to files
that are sent or received from CloudLayer storage resources."""
    folder: str
    hash_: str
