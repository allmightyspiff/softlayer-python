from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Invoice_Item(Entity):
    """Each billing invoice item makes up a record within an invoice. This provides you with a detailed record of
everything related to an invoice item. When you are billed, our system takes active billing items and creates
an invoice. These invoice items are a copy of your active billing items, and make up the contents of your
invoice."""
    associatedInvoiceItemId: int
    billingItemId: int
    categoryCode: str
    createDate: datetime
    description: str
    domainName: str
    endDate: datetime
    hostName: str
    hourlyRecurringFee: float
    id_: int
    invoiceId: int
    laborAfterTaxAmount: float
    laborFee: float
    laborFeeTaxRate: float
    laborTaxAmount: float
    notes: str
    oneTimeAfterTaxAmount: float
    oneTimeFee: float
    oneTimeFeeTaxRate: float
    oneTimeTaxAmount: float
    packageId: int
    parentId: int
    productItemId: int
    recurringAfterTaxAmount: float
    recurringFee: float
    recurringFeeTaxRate: float
    recurringTaxAmount: float
    resourceTableId: int
    serviceProviderId: int
    setupAfterTaxAmount: float
    setupFee: float
    setupFeeDeferralMonths: int
    setupFeeTaxRate: float
    setupTaxAmount: float

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Invoice_Item'

    def getObject(self, identifier: int) -> 'Billing_Invoice_Item':
        """Retrieve a SoftLayer_Billing_Invoice_Item record."""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getObject', id=identifier)
        return data

    def getAssociatedChildren(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getAssociatedChildren', id=identifier)
        return data

    def getAssociatedInvoiceItem(self, identifier: int) -> 'Billing_Invoice_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getAssociatedInvoiceItem', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCategory(self, identifier: int) -> 'Product_Item_Category':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getChildren(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getChildren', id=identifier)
        return data

    def getDPart(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getDPart', id=identifier)
        return data

    def getFilteredAssociatedChildren(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getFilteredAssociatedChildren', id=identifier)
        return data

    def getHourlyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getHourlyFlag', id=identifier)
        return data

    def getInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getNonZeroAssociatedChildren(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getNonZeroAssociatedChildren', id=identifier)
        return data

    def getParent(self, identifier: int) -> 'Billing_Invoice_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getParent', id=identifier)
        return data

    def getProduct(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getProduct', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getTopLevelProductGroupName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getTopLevelProductGroupName', id=identifier)
        return data

    def getTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getTotalOneTimeAmount', id=identifier)
        return data

    def getTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getTotalOneTimeTaxAmount', id=identifier)
        return data

    def getTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getTotalRecurringAmount', id=identifier)
        return data

    def getTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getTotalRecurringTaxAmount', id=identifier)
        return data

    def getUsageChargeFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice_Item', 'getUsageChargeFlag', id=identifier)
        return data
