from SoftLayer.sltypes.Entity import Entity

class User_Preference_Type(Entity):
    """The SoftLayer_User_Preference_Type data type contains a single preference type including the accepted values."""
    description: str
    keyName: str
    name: str
    valueExample: str
