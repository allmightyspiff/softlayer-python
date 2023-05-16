# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Order_Quote(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Order_Quote'
        self.client = client

    def claim(
        self,
        quoteKey: str,
        quoteId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'claim',
            quoteKey,
            quoteId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def deleteQuote(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'deleteQuote',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getPdf(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdf',
            id=identifier
        )
        
        return data


    def getQuoteByQuoteKey(
        self,
        quoteKey: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'getQuoteByQuoteKey',
            quoteKey,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getRecalculatedOrderContainer(
        self,
        userOrderData: 'SoftLayer_Container_Product_Order',
        orderBeingPlacedFlag: bool,
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'getRecalculatedOrderContainer',
            userOrderData,
            orderBeingPlacedFlag,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def placeOrder(
        self,
        orderData: 'SoftLayer_Container_Product_Order',
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order_Receipt':

        data = self.client.call(
            self.service,
            'placeOrder',
            orderData,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return Receipt(data)


    def placeQuote(
        self,
        orderData: 'SoftLayer_Container_Product_Order',
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'placeQuote',
            orderData,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def saveQuote(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'saveQuote',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def verifyOrder(
        self,
        orderData: 'SoftLayer_Container_Product_Order',
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'verifyOrder',
            orderData,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def withdrawGdprAcceptance(
        self,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'withdrawGdprAcceptance',
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getDoNotContactFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDoNotContactFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrder(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':

        data = self.client.call(
            self.service,
            'getOrder',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


    def getOrdersFromQuote(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order]':

        data = self.client.call(
            self.service,
            'getOrdersFromQuote',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


