from SoftLayer.sltypes.Entity import Entity

class Product_Item_Rule_Resource(Entity):
    """The item rule resource data type represents a resource that is part of an item rule. The item rule resource
is used when its item rule is checked on an order."""
    id_: int
    resourceTableId: int
    ruleId: int
