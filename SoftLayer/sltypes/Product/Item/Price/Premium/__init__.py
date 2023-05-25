from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item_Price_Premium(Entity):
    hourlyModifier: float
    itemPriceId: int
    locationId: int
    monthlyModifier: float
    packageId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item_Price_Premium'

    def getObject(self, identifier: int) -> 'Product_Item_Price_Premium':
        """Retrieve a SoftLayer_Product_Item_Price_Premium record."""
        data = self.client.call('SoftLayer_Product_Item_Price_Premium', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Premium import Product_Item_Price_Premium
        return data

    def getItemPrice(self, identifier: int) -> 'Product_Item_Price':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price_Premium', 'getItemPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price_Premium', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getPackage(self, identifier: int) -> 'Product_Package':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price_Premium', 'getPackage', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data
