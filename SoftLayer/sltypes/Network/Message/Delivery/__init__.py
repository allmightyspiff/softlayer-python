from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Message_Delivery(Entity):
    accountId: int
    createDate: datetime
    guid: str
    id_: int
    modifyDate: datetime
    password: str
    typeId: int
    username: str
    vendorId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Message_Delivery'

    def editObject(self, identifier: int, templateObject: 'Network_Message_Delivery') -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Message_Delivery':
        """Retrieve a SoftLayer_Network_Message_Delivery record."""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Message_Delivery import Network_Message_Delivery
        return data

    def getUpgradeItemPrices(self, identifier: int) -> list['Product_Item_Price']:
        """Retrieve available upgrade prices"""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getUpgradeItemPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getType(self, identifier: int) -> 'Network_Message_Delivery_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Message_Delivery_Type import Network_Message_Delivery_Type
        return data

    def getVendor(self, identifier: int) -> 'Network_Message_Delivery_Vendor':
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery', 'getVendor', id=identifier)
        from SoftLayer.sltypes.Network_Message_Delivery_Vendor import Network_Message_Delivery_Vendor
        return data
