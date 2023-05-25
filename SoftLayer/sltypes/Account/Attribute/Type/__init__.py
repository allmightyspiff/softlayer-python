from SoftLayer.sltypes.Entity import Entity

class Account_Attribute_Type(Entity):
    """SoftLayer_Account_Attribute_Type models the type of attribute that can be assigned to a SoftLayer customer
account."""
    description: str
    id_: int
    keyName: str
    name: str
