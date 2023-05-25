from SoftLayer.sltypes.Entity import Entity

class Product_Item_Price_Attribute(Entity):
    id_: int
    itemPriceAttributeTypeId: int
    itemPriceId: int
    value: str
