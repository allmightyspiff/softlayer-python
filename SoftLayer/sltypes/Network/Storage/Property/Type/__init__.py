from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Property_Type(Entity):
    """The storage property types provide standard definitions for properties which can be used with any type for
Storage offering.  The properties provide additional information about a volume which they are assigned to."""
    description: str
    keyname: str
    name: str
