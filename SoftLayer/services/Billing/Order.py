# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Order(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Order'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def approveModifiedOrder(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'approveModifiedOrder',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def getOrderStatuses(
        self,
        
    ) -> 'list[SoftLayer_Container_Billing_Order_Status]':
        data = self.client.call(
            self.service,
            'getOrderStatuses',
            
        )
        from SoftLayer.datatypes.Container.Billing.Order.Status import Status
        return SL_Status(data)

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
    def getPdfFilename(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPdfFilename',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getRecalculatedOrderContainer(
        self,
        message: str,
        ignoreDiscountsFlag: boolean
    ) -> 'SoftLayer_Container_Product_Order':
        data = self.client.call(
            self.service,
            'getRecalculatedOrderContainer',
            message,
            ignoreDiscountsFlag
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return SL_Order(data)

# This file was automatically generated with tools/generateTypes.py
    def getReceipt(
        self,
        
    ) -> 'SoftLayer_Container_Product_Order_Receipt':
        data = self.client.call(
            self.service,
            'getReceipt',
            
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return SL_Receipt(data)

# This file was automatically generated with tools/generateTypes.py
    def isPendingEditApproval(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isPendingEditApproval',
            
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
    def getBrand(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':
        data = self.client.call(
            self.service,
            'getBrand',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
    def getCart(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Cart':
        data = self.client.call(
            self.service,
            'getCart',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Cart import Cart
        return SL_Cart(data)

# This file was automatically generated with tools/generateTypes.py
    def getCoreRestrictedItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':
        data = self.client.call(
            self.service,
            'getCoreRestrictedItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getCreditCardTransactions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_Card_Transaction]':
        data = self.client.call(
            self.service,
            'getCreditCardTransactions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.Card.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getExchangeRate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':
        data = self.client.call(
            self.service,
            'getExchangeRate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return SL_ExchangeRate(data)

# This file was automatically generated with tools/generateTypes.py
    def getInitialInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':
        data = self.client.call(
            self.service,
            'getInitialInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return SL_Invoice(data)

# This file was automatically generated with tools/generateTypes.py
    def getItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':
        data = self.client.call(
            self.service,
            'getItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getOrderApprovalDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':
        data = self.client.call(
            self.service,
            'getOrderApprovalDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderNonServerMonthlyAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderNonServerMonthlyAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderServerMonthlyAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderServerMonthlyAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTopLevelItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':
        data = self.client.call(
            self.service,
            'getOrderTopLevelItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalOneTime(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalOneTime',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalOneTimeAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalOneTimeAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalOneTimeTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalOneTimeTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalRecurring(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalRecurring',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalRecurringAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalRecurringAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalRecurringTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalRecurringTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderTotalSetupAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':
        data = self.client.call(
            self.service,
            'getOrderTotalSetupAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOrderType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Type':
        data = self.client.call(
            self.service,
            'getOrderType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getPaypalTransactions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_PayPal_Transaction]':
        data = self.client.call(
            self.service,
            'getPaypalTransactions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.PayPal.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getPresaleEvent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Sales_Presale_Event':
        data = self.client.call(
            self.service,
            'getPresaleEvent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getQuote(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Quote':
        data = self.client.call(
            self.service,
            'getQuote',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def getReferralPartner(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getReferralPartner',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getUpgradeRequestFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getUpgradeRequestFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getUserRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getUserRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


