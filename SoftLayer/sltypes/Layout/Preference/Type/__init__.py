from SoftLayer.sltypes.Entity import Entity

class Layout_Preference_Type(Entity):
    """The SoftLayer_Layout_Preference_Type contains definitions for preference types"""
    id_: int
    keyname: str
    name: str
    valueExpression: str
