from SoftLayer.sltypes.Entity import Entity

class Network_Regional_Internet_Registry(Entity):
    """Regional Internet Registries are the organizations who delegate IP address blocks to other groups or
organizations around the Internet. The information contained in this data type is used throughout the
networking-related services in our systems."""
    id_: int
    keyName: str
    name: str
