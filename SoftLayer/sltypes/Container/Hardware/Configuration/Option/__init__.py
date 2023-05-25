from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Product.Package.Preset import Product_Package_Preset
from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Entity import Entity

class Container_Hardware_Configuration_Option(Entity):
    """An option found within a [[SoftLayer_Container_Hardware_Configuration (type)]] structure."""
    itemPrice: Product_Item_Price
    preset: Product_Package_Preset
    template: Hardware
