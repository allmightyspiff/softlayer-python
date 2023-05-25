from SoftLayer.sltypes.Entity import Entity

class Network_Service_Resource(Entity):
    """The SoftLayer_Network_Service_Resource is used to store information related to a service.  It is used for
determining the correct resource to connect to for a given service, like NAS, Evault, etc."""
    backendIpAddress: str
    frontendIpAddress: str
    id_: int
    name: str
