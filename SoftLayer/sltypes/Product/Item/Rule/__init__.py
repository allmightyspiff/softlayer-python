from SoftLayer.sltypes.Entity import Entity

class Product_Item_Rule(Entity):
    """The item rule data type represents a rule that must be followed when the item assigned to the rule is
ordered. The type and operation applied to the resources of the rule will affect how the rule is checked
during ordering."""
    itemId: int
    message: str
    operation: str
    packageId: int
    typeId: int
