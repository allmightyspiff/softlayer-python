from SoftLayer.sltypes.Entity import Entity

class Account_Attribute(Entity):
    """Many SoftLayer customer accounts have individual attributes assigned to them that describe features or
special features for that account, such as special pricing, account statuses, and ordering instructions. The
SoftLayer_Account_Attribute data type contains information relating to a single SoftLayer_Account attribute."""
    accountAttributeTypeId: int
    accountId: int
    id_: int
    value: str
