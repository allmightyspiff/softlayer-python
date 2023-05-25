from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Product.Item import Product_Item
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Item_Discount_Program(Entity):
    """The SoftLayer_Container_Product_Item_Discount_Program data type represents the information about a discount
that is related to a specific product item."""
    applicableQuantity: int
    item: Product_Item
    oneTimeAmount: float
    oneTimeTax: float
    prices: list[Product_Item_Price]
    proratedOneTimeAmount: float
    proratedOneTimeTax: float
    proratedRecurringAmount: float
    proratedRecurringTax: float
    recurringAmount: float
    recurringTax: float
