from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Hub_ObjectStorage_Endpoint(Entity):
    """SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Endpoint provides specific details on available
endpoint URLs and locations."""
    legacy: bool
    location: str
    region: str
    type_: str
    url: str
