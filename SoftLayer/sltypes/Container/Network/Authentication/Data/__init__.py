from SoftLayer.sltypes.Entity import Entity

class Container_Network_Authentication_Data(Entity):
    """This object holds authentication data to a server."""
    host: str
    password: str
    port: int
    type_: str
    username: str
