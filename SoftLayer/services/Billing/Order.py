# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Order(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Order'
        self.client = client

    def approveModifiedOrder(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'approveModifiedOrder',
            
        )
        
        return data


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
        return Order(data)


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
        return Order(data)


    def getOrderStatuses(
        self,
        
    ) -> 'list[SoftLayer_Container_Billing_Order_Status]':

        data = self.client.call(
            self.service,
            'getOrderStatuses',
            
        )
        from SoftLayer.datatypes.Container.Billing.Order.Status import Status
        return Status(data)


    def getPdf(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdf',
            
        )
        
        return data


    def getPdfFilename(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPdfFilename',
            
        )
        
        return data


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
        return Order(data)


    def getReceipt(
        self,
        
    ) -> 'SoftLayer_Container_Product_Order_Receipt':

        data = self.client.call(
            self.service,
            'getReceipt',
            
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return Receipt(data)


    def isPendingEditApproval(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPendingEditApproval',
            
        )
        
        return data


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
        return Brand(data)


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
        return Cart(data)


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
        return Item(data)


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
        return Transaction(data)


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
        return ExchangeRate(data)


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
        return Invoice(data)


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
        return Item(data)


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
        return Item(data)


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
        return Type(data)


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
        return Transaction(data)


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
        return Event(data)


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
        return Quote(data)


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
        return Account(data)


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
        return Customer(data)


