from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_ConsoleData(Entity):
    """The SoftLayer_Container_Virtual_ConsoleData data type contains information used to access a VSIs console"""
    websocketHost: str
    websocketPath: str
    websocketPort: str
    websocketToken: str
