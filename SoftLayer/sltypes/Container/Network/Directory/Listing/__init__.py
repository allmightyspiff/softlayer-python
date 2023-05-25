from SoftLayer.sltypes.Entity import Entity

class Container_Network_Directory_Listing(Entity):
    """SoftLayer_Container_Network_Directory_Listing represents a single entry in a listing of files within a remote
directory. API methods that return remote directory listings typically return arrays of
SoftLayer_Container_Network_Directory_Listing objects."""
    fileCount: int
    name: str
    type_: str
