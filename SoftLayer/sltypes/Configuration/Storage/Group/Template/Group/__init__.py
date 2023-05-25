from SoftLayer.sltypes.Entity import Entity

class Configuration_Storage_Group_Template_Group(Entity):
    """Single storage group(array) used in a storage group template.   If a server configuration requires a raid
configuration this object will describe a single array to be configured."""
    diskControllerIndex: int
    grow: bool
    hardDrivesString: str
    hotSpareDrivesString: str
    orderIndex: int
    size: float
