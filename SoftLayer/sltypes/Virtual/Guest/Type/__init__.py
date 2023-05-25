from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Type(Entity):
    """SoftLayer_Virtual_Guest_Type models the type of a [[SoftLayer_Virtual_Guest]] (PUBLIC | DEDICATED | PRIVATE)"""
    id_: int
    keyName: str
    name: str
