from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Host(Entity):
    """The SoftLayer_Container_Network_Storage_Host will contain the reference id field for the object associated
with the host.  The host object type will also be returned."""
    id_: int
    objectType: str
