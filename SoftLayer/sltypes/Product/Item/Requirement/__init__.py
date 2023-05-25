from SoftLayer.sltypes.Entity import Entity

class Product_Item_Requirement(Entity):
    """The SoftLayer_Product_Item_Requirement data type contains information relating to what requirements, if any,
exist for an item. The requiredItemId local property is the item id that is required."""
    id_: int
    itemId: int
    message: str
    requiredItemId: int
