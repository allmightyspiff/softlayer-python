from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Product_Catalog_Item_Price(Entity):
    """The SoftLayer_Product_Catalog_Item_Price type assigns an Item Price to a Catalog. This relation defines the
composition of Item Prices in a Catalog."""
    catalogId: int
    createDate: datetime
    modifyDate: datetime
    priceId: int
