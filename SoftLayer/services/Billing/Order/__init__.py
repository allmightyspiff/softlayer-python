# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Order(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Order'
        self.client = client

    def approveModifiedOrder(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'approveModifiedOrder',
            id=identifier
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
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
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
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdf',
            id=identifier
        )
        
        return data


    def getPdfFilename(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPdfFilename',
            id=identifier
        )
        
        return data


    def getRecalculatedOrderContainer(
        self,
        message: str,
        ignoreDiscountsFlag: bool,
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order':

        data = self.client.call(
            self.service,
            'getRecalculatedOrderContainer',
            message,
            ignoreDiscountsFlag,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order import Order
        return Order(data)


    def getReceipt(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Product_Order_Receipt':

        data = self.client.call(
            self.service,
            'getReceipt',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Order.Receipt import Receipt
        return Receipt(data)


    def isPendingEditApproval(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPendingEditApproval',
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


    def getBrand(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getBrand',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getCart(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Cart':

        data = self.client.call(
            self.service,
            'getCart',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Cart import Cart
        return Cart(data)


    def getCoreRestrictedItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':

        data = self.client.call(
            self.service,
            'getCoreRestrictedItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return Item(data)


    def getCreditCardTransactions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_Card_Transaction]':

        data = self.client.call(
            self.service,
            'getCreditCardTransactions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.Card.Transaction import Transaction
        return Transaction(data)


    def getExchangeRate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':

        data = self.client.call(
            self.service,
            'getExchangeRate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


    def getInitialInvoice(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getInitialInvoice',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':

        data = self.client.call(
            self.service,
            'getItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return Item(data)


    def getOrderApprovalDate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getOrderApprovalDate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderNonServerMonthlyAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderNonServerMonthlyAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderServerMonthlyAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderServerMonthlyAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTopLevelItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Item]':

        data = self.client.call(
            self.service,
            'getOrderTopLevelItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Item import Item
        return Item(data)


    def getOrderTotalAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalOneTime(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalOneTime',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalOneTimeAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalOneTimeAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalOneTimeTaxAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalOneTimeTaxAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalRecurring(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalRecurring',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalRecurringAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalRecurringAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalRecurringTaxAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalRecurringTaxAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderTotalSetupAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getOrderTotalSetupAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Type':

        data = self.client.call(
            self.service,
            'getOrderType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Type import Type
        return Type(data)


    def getPaypalTransactions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_PayPal_Transaction]':

        data = self.client.call(
            self.service,
            'getPaypalTransactions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.PayPal.Transaction import Transaction
        return Transaction(data)


    def getPresaleEvent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Sales_Presale_Event':

        data = self.client.call(
            self.service,
            'getPresaleEvent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


    def getQuote(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order_Quote':

        data = self.client.call(
            self.service,
            'getQuote',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getReferralPartner(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getReferralPartner',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getUpgradeRequestFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getUpgradeRequestFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getUserRecord(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUserRecord',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


