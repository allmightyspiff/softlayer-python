from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Location import Location
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Network_Storage_Hub_Datacenter(Entity):
    """This class is used to contain a datacenter location and its associated active usage rate prices for object
storage ordering."""
    location: Location
    usageRatePrices: list[Product_Item_Price]
