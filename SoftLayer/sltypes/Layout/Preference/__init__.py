from SoftLayer.sltypes.Entity import Entity

class Layout_Preference(Entity):
    """The SoftLayer_Layout_Preference contains definitions for default layout item preferences"""
    id_: int
    layoutPreferenceTypeId: int
    value: str
