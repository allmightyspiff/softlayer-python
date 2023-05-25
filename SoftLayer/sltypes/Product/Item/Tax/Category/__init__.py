from SoftLayer.sltypes.Entity import Entity

class Product_Item_Tax_Category(Entity):
    """The SoftLayer_Product_Item_Tax_Category data type contains the tax categories that are associated with
products."""
    id_: int
    keyName: str
    name: str
    statusFlag: int
