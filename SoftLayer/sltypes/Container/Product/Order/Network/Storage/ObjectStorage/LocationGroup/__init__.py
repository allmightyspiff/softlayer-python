from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Location.Group import Location_Group
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup(Entity):
    """This class is used to contain a location group and its associated active usage rate prices for object storage
ordering."""
    clusterGeolocationType: str
    locationGroup: Location_Group
    usageRatePrices: list[Product_Item_Price]
