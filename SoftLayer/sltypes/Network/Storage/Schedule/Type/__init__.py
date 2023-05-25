from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Schedule_Type(Entity):
    """A schedule type is used to define what a schedule was created to do. When creating a schedule to take
snapshots of a volume, the 'Snapshot' schedule type would be used."""
    id_: int
    keyname: str
    name: str
