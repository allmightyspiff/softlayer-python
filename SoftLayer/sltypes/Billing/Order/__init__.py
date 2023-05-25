from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Order(Entity):
    """The SoftLayer_Billing_Order data type contains general information relating to an individual order applied to
a SoftLayer customer account or to a new customer. Personal information in this type such as names,
addresses, and phone numbers are taken from the account's contact information at the time the order is
generated for existing SoftLayer customer."""
    accountId: int
    createDate: datetime
    id_: int
    impersonatingUserRecordId: int
    modifyDate: datetime
    orderQuoteId: int
    orderTypeId: int
    presaleEventId: int
    privateCloudOrderFlag: bool
    status: str
    userRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Order'

    def approveModifiedOrder(self, identifier: int) -> bool:
        """Approve the changes of a modified order"""
        data = self.client.call('SoftLayer_Billing_Order', 'approveModifiedOrder', id=identifier)
        return data

    def getAllObjects(self) -> list['Billing_Order']:
        """Get all billing orders for your account"""
        data = self.client.call('SoftLayer_Billing_Order', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Billing_Order':
        """Retrieve a SoftLayer_Billing_Order record."""
        data = self.client.call('SoftLayer_Billing_Order', 'getObject', id=identifier)
        return data

    def getOrderStatuses(self) -> list['Container_Billing_Order_Status']:
        """Get a list of SoftLayer_Container_Billing_Order_Status objects."""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderStatuses')
        from SoftLayer.sltypes.Container_Billing_Order_Status import Container_Billing_Order_Status
        return data

    def getPdf(self, identifier: int) -> str:
        """Retrieve a PDF copy of a quote."""
        data = self.client.call('SoftLayer_Billing_Order', 'getPdf', id=identifier)
        return data

    def getPdfFilename(self, identifier: int) -> str:
        """Retrieve the default name of the PDF"""
        data = self.client.call('SoftLayer_Billing_Order', 'getPdfFilename', id=identifier)
        return data

    def getRecalculatedOrderContainer(self, identifier: int, message: str, ignoreDiscountsFlag: bool) -> 'Container_Product_Order':
        """Generate an [[SoftLayer_Container_Product_Order|order container]] from a billing order."""
        data = self.client.call('SoftLayer_Billing_Order', 'getRecalculatedOrderContainer', message, ignoreDiscountsFlag, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def getReceipt(self, identifier: int) -> 'Container_Product_Order_Receipt':
        """Generate and return an order receipt."""
        data = self.client.call('SoftLayer_Billing_Order', 'getReceipt', id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Receipt import Container_Product_Order_Receipt
        return data

    def isPendingEditApproval(self, identifier: int) -> bool:
        """Determine if the existing order is pending edit approval"""
        data = self.client.call('SoftLayer_Billing_Order', 'isPendingEditApproval', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getCart(self, identifier: int) -> 'Billing_Order_Cart':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getCart', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Cart import Billing_Order_Cart
        return data

    def getCoreRestrictedItems(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getCoreRestrictedItems', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getCreditCardTransactions(self, identifier: int) -> list['Billing_Payment_Card_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getCreditCardTransactions', id=identifier)
        from SoftLayer.sltypes.Billing_Payment_Card_Transaction import Billing_Payment_Card_Transaction
        return data

    def getExchangeRate(self, identifier: int) -> 'Billing_Currency_ExchangeRate':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getExchangeRate', id=identifier)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data

    def getInitialInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getInitialInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getItems(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getItems', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getOrderApprovalDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderApprovalDate', id=identifier)
        return data

    def getOrderNonServerMonthlyAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderNonServerMonthlyAmount', id=identifier)
        return data

    def getOrderServerMonthlyAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderServerMonthlyAmount', id=identifier)
        return data

    def getOrderTopLevelItems(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTopLevelItems', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getOrderTotalAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalAmount', id=identifier)
        return data

    def getOrderTotalOneTime(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalOneTime', id=identifier)
        return data

    def getOrderTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalOneTimeAmount', id=identifier)
        return data

    def getOrderTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalOneTimeTaxAmount', id=identifier)
        return data

    def getOrderTotalRecurring(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalRecurring', id=identifier)
        return data

    def getOrderTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalRecurringAmount', id=identifier)
        return data

    def getOrderTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalRecurringTaxAmount', id=identifier)
        return data

    def getOrderTotalSetupAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderTotalSetupAmount', id=identifier)
        return data

    def getOrderType(self, identifier: int) -> 'Billing_Order_Type':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getOrderType', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Type import Billing_Order_Type
        return data

    def getPaypalTransactions(self, identifier: int) -> list['Billing_Payment_PayPal_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getPaypalTransactions', id=identifier)
        from SoftLayer.sltypes.Billing_Payment_PayPal_Transaction import Billing_Payment_PayPal_Transaction
        return data

    def getPresaleEvent(self, identifier: int) -> 'Sales_Presale_Event':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getPresaleEvent', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getQuote(self, identifier: int) -> 'Billing_Order_Quote':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getQuote', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getReferralPartner(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getReferralPartner', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getUpgradeRequestFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getUpgradeRequestFlag', id=identifier)
        return data

    def getUserRecord(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Billing_Order', 'getUserRecord', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
