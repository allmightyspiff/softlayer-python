# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Message_Delivery(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Message_Delivery'
        self.client = client

    def editObject(
        self,
        templateObject: SoftLayer_Network_Message_Delivery
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery import Delivery
        return Delivery(data)


    def getUpgradeItemPrices(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Type import Type
        return Type(data)


    def getVendor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Vendor':

        data = self.client.call(
            self.service,
            'getVendor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Vendor import Vendor
        return Vendor(data)


