from SoftLayer.sltypes.Entity import Entity

class Product_Package_Items(Entity):
    """This data type is a cross-reference between the SoftLayer_Product_Package and the SoftLayer_Product_Item(s)
that belong in the SoftLayer_Product_Package."""
    id_: str
    itemId: int
    packageId: int
