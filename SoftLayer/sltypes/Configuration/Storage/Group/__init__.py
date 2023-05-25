from SoftLayer.sltypes.Entity import Entity

class Configuration_Storage_Group(Entity):
    """This class describes the base Storage Group for a Complex Drive Configuration"""
    description: str
    diskSpace: float
    id_: int
    lvmFlag: bool
    name: str
    units: str
