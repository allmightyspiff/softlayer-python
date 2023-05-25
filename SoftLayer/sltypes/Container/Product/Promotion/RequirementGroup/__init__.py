from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Product.Package.Preset import Product_Package_Preset
from SoftLayer.sltypes.Product.Item.Category import Product_Item_Category
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Promotion_RequirementGroup(Entity):
    """The SoftLayer_Container_Product_Promotion_RequirementGroup data type contains the required options that must
be present on an order for the promotion to be applied. At least one of the categories, presets, or prices
must be on the order."""
    categories: list[Product_Item_Category]
    presets: list[Product_Package_Preset]
    prices: list[Product_Item_Price]
