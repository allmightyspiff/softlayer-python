from SoftLayer.sltypes.Entity import Entity

class Container_RemoteManagement_PmInfo(Entity):
    """The SoftLayer_Container_RemoteManagement_PmInfo contains pminfo information retrieved from a server's remote
management card."""
    pmInfoId: str
    pmInfoReading: str
