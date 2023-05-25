from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Order_Quote(Entity):
    """The SoftLayer_Billing_Oder_Quote data type contains general information relating to an individual order
applied to a SoftLayer customer account or to a new customer. Personal information in this type such as
names, addresses, and phone numbers are taken from the account's contact information at the time the quote is
generated for existing SoftLayer customer."""
    accountId: int
    completedPurchaseDataId: int
    createDate: datetime
    expirationDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    publicNote: str
    quoteKey: str
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Order_Quote'

    def claim(self, quoteKey: str, quoteId: int) -> 'Billing_Order_Quote':
        """Claim an anonymous quote"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'claim', quoteKey, quoteId)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def deleteQuote(self, identifier: int) -> 'Billing_Order_Quote':
        """Delete the quote of an order"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'deleteQuote', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getObject(self, identifier: int) -> 'Billing_Order_Quote':
        """Retrieve a SoftLayer_Billing_Order_Quote record."""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getPdf(self, identifier: int) -> str:
        """Retrieve a PDF copy of a quote."""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getPdf', id=identifier)
        return data

    def getQuoteByQuoteKey(self, quoteKey: str) -> 'Billing_Order_Quote':
        """Retrieve a [[SoftLayer_Billing_Order_Quote]] by the quote key specified."""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getQuoteByQuoteKey', quoteKey)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getRecalculatedOrderContainer(self, identifier: int, userOrderData: 'Container_Product_Order', orderBeingPlacedFlag: bool) -> 'Container_Product_Order':
        """Generate an [[SoftLayer_Container_Product_Order|order container]] from the previously-created quote."""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getRecalculatedOrderContainer', userOrderData, orderBeingPlacedFlag, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def placeOrder(self, identifier: int, orderData: 'Container_Product_Order') -> 'Container_Product_Order_Receipt':
        """Place an order"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'placeOrder', orderData, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Receipt import Container_Product_Order_Receipt
        return data

    def placeQuote(self, identifier: int, orderData: 'Container_Product_Order') -> 'Container_Product_Order':
        """Saves changes to a quote"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'placeQuote', orderData, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def saveQuote(self, identifier: int) -> 'Billing_Order_Quote':
        """Save the quote of an order"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'saveQuote', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def verifyOrder(self, identifier: int, orderData: 'Container_Product_Order') -> 'Container_Product_Order':
        """Verify an order"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'verifyOrder', orderData, id=identifier)
        from SoftLayer.sltypes.Container_Product_Order import Container_Product_Order
        return data

    def withdrawGdprAcceptance(self, identifier: int) -> None:
        """Withdraws the users acceptance of the GDPR terms."""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'withdrawGdprAcceptance', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDoNotContactFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getDoNotContactFlag', id=identifier)
        return data

    def getOrder(self, identifier: int) -> 'Billing_Order':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getOrder', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getOrdersFromQuote(self, identifier: int) -> list['Billing_Order']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Quote', 'getOrdersFromQuote', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data
