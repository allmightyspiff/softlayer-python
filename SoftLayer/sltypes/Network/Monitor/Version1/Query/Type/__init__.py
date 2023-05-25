from SoftLayer.sltypes.Entity import Entity

class Network_Monitor_Version1_Query_Type(Entity):
    """The MonitorType type stores a name, long description, and default arguments for the monitor types.  The only
use for this object is in reference.  The user chooses a monitoring type that would be appropriate for their
server, and sets the id of the Query_Type to SoftLayer_Network_Monitor_Version1_Query_Host->queryTypeId   The
user can retrieve all available Query Types with the getAllObjects method on this service."""
    argumentDescription: str
    description: str
    id_: int
    monitorLevel: int
    name: str
