from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Type(Entity):
    """The SoftLayer_Hardware_Component_Type data type provides details on the type of component requested"""
    id_: int
    keyName: str
    type_: str
    typeParentId: int
