from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Sales_Presale_Event(Entity):
    """The presale event data types indicate the information regarding an individual presale event. The
'''locationId''' will indicate the datacenter associated with the presale event. The '''itemId''' will
indicate the product item associated with a particular presale event - however these are more rare. The
'''startDate''' and '''endDate''' will provide information regarding when the presale event is available for
use. At the end of the presale event, the server or services purchased will be available once approved and
provisioned."""
    description: str
    endDate: datetime
    id_: int
    itemId: int
    locationId: int
    startDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Sales_Presale_Event'

    def getAllObjects(self) -> list['Sales_Presale_Event']:
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getAllObjects')
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getObject(self, identifier: int) -> 'Sales_Presale_Event':
        """Retrieve a SoftLayer_Sales_Presale_Event record."""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getObject', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getActiveFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getActiveFlag', id=identifier)
        return data

    def getExpiredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getExpiredFlag', id=identifier)
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getOrders(self, identifier: int) -> list['Billing_Order']:
        """"""
        data = self.client.call('SoftLayer_Sales_Presale_Event', 'getOrders', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data
