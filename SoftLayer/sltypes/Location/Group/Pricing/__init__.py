from SoftLayer.sltypes.Location.Group import Location_Group
from SoftLayer.sltypes.Location_Group import Location_Group
from SoftLayer import BaseClient

class Location_Group_Pricing(Location_Group):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Group_Pricing'

    def getAllObjects(self) -> list['Location_Group']:
        """Get all pricing location groups."""
        data = self.client.call('SoftLayer_Location_Group_Pricing', 'getAllObjects')
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getObject(self, identifier: int) -> 'Location_Group_Pricing':
        """Retrieve a SoftLayer_Location_Group_Pricing record."""
        data = self.client.call('SoftLayer_Location_Group_Pricing', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location_Group_Pricing import Location_Group_Pricing
        return data

    def getPrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Location_Group_Pricing', 'getPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data
