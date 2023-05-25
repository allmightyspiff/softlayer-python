from SoftLayer.sltypes.Entity import Entity

class Product_Item_Bundles(Entity):
    """The SoftLayer_Product_Item_Bundles contains item to price cross references. Relates a category, price and
item to a bundle.  Match bundle ids to see all items and prices in a particular bundle."""
    bundleItemId: int
    id_: int
    itemPriceId: int
