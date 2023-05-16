# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Order_Quote(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Order_Quote'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteQuote(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':
        data = self.client.call(
            self.service,
            'deleteQuote',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Quote':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def getPdf(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPdf',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def getRecalculatedOrderContainer(
        self,
        userOrderData: SoftLayer_Container_Product_Order,
        orderBeingPlacedFlag: boolean
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'getRecalculatedOrderContainer',
            userOrderData,
            orderBeingPlacedFlag
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def placeOrder(
        self,
        orderData: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order_Receipt':
        data = self.client.call(
            self.service,
            'placeOrder',
            orderData
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return SL_Receipt(data)

# This file was automatically generated with tools/generateTypes.py
    def placeQuote(
        self,
        orderData: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'placeQuote',
            orderData
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def saveQuote(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Order_Quote':
        data = self.client.call(
            self.service,
            'saveQuote',
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def verifyOrder(
        self,
        orderData: SoftLayer_Container_Product_Order
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'verifyOrder',
            orderData
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def withdrawGdprAcceptance(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'withdrawGdprAcceptance',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getDoNotContactFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getDoNotContactFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrder(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':
        data = self.client.call(
            self.service,
            'getOrder',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def getOrdersFromQuote(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order]':
        data = self.client.call(
            self.service,
            'getOrdersFromQuote',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return SL_Order(data)


