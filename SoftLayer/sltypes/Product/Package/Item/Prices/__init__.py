from SoftLayer.sltypes.Entity import Entity

class Product_Package_Item_Prices(Entity):
    """The SoftLayer_Product_Package_Item_Prices contains price to package cross references Relates a category,
price and item to a bundle.  Match bundle ids to see all items and prices in a particular bundle."""
    id_: int
    itemPriceId: int
    packageId: int
