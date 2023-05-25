from SoftLayer.sltypes.Entity import Entity

class Product_Item_Attribute(Entity):
    """The [[SoftLayer_Product_Item_Attribute]] data type allows us to describe a [[SoftLayer_Product_Item]] by
attaching specific attributes, which may dictate how it interacts with other products and services. Most, if
not all, of these attributes are geared towards internal usage, so customers should rarely be concerned with
them."""
    id_: int
    itemAttributeTypeId: int
    itemId: int
    value: str
