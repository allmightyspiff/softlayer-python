from SoftLayer.sltypes.Entity import Entity

class Product_Item_Category_Order_Option_Type(Entity):
    """The SoftLayer_Product_Item_Category_Order_Option_Type data type contains options that can be applied to
orders for prices."""
    description: str
    id_: int
    keyname: str
    name: str
    value: str
