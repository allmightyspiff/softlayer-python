from SoftLayer.sltypes.Entity import Entity

class Product_Item_Attribute_Type(Entity):
    """The [[SoftLayer_Product_Item_Attribute_Type]] data type defines the available type of product attributes that
are available. This allows for convenient reference to a [[SoftLayer_Product_Item_Attribute|product
attribute]] by a unique key name value."""
    keyName: str
    name: str
