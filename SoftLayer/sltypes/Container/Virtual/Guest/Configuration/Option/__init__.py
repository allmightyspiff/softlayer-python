from SoftLayer.sltypes.Virtual.Guest import Virtual_Guest
from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Product.Package.Preset import Product_Package_Preset
from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_Guest_Configuration_Option(Entity):
    """An option found within a [[SoftLayer_Container_Virtual_Guest_Configuration (type)]] structure."""
    flavor: Product_Package_Preset
    itemPrice: Product_Item_Price
    template: Virtual_Guest
