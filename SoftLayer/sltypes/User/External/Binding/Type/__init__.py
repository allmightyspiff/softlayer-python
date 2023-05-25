from SoftLayer.sltypes.Entity import Entity

class User_External_Binding_Type(Entity):
    """The SoftLayer_User_External_Binding_Type data type contains information relating to a type of external
authentication binding.  It contains a user friendly name as well as a unique key name."""
    keyName: str
    name: str
