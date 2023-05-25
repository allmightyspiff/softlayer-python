from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Invoice(Entity):
    """The SoftLayer_Billing_Invoice data type contains general information relating to an individual invoice
applied to a SoftLayer customer account. Personal information in this type such as names, addresses, and
phone numbers are taken from the account's contact information at the time the invoice is generated."""
    accountId: int
    address1: str
    address2: str
    city: str
    claimedTaxExemptTxFlag: bool
    closedDate: datetime
    companyName: str
    country: str
    createDate: datetime
    creditTypeDetailId: int
    documentsGeneratedFlag: bool
    email: str
    endingBalance: float
    faxPhone: str
    firstName: str
    id_: int
    lastName: str
    modifyDate: datetime
    officePhone: str
    postalCode: str
    purchaseOrderNumber: str
    startingBalance: float
    state: str
    statusCode: str
    taxStatusId: int
    taxTypeId: int
    typeCode: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Invoice'

    def emailInvoices(self, options: 'Container_Billing_Invoice_Email') -> None:
        """Create a transaction to email invoice links."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'emailInvoices', options)
        return data

    def getExcel(self, identifier: int) -> str:
        """Retrieve a Microsoft Excel copy of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getExcel', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Billing_Invoice':
        """Retrieve a SoftLayer_Billing_Invoice record."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getPdf(self, identifier: int) -> str:
        """Retrieve a PDF copy of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPdf', id=identifier)
        return data

    def getPdfDetailed(self, identifier: int) -> str:
        """Retrieve a PDF copy of the detailed invoice summary."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPdfDetailed', id=identifier)
        return data

    def getPdfDetailedFilename(self, identifier: int) -> str:
        """Get the name of the detailed version of the PDF."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPdfDetailedFilename', id=identifier)
        return data

    def getPdfFileSize(self, identifier: int) -> int:
        """Retrieve the size of a PDF copy of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPdfFileSize', id=identifier)
        return data

    def getPdfFilename(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPdfFilename', id=identifier)
        return data

    def getPreliminaryExcel(self, identifier: int) -> str:
        """Retrieve a Microsoft Excel copy of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPreliminaryExcel', id=identifier)
        return data

    def getPreliminaryPdf(self, identifier: int) -> str:
        """Retrieve a PDF copy of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPreliminaryPdf', id=identifier)
        return data

    def getPreliminaryPdfDetailed(self, identifier: int) -> str:
        """Retrieve a PDF copy of the detailed version of an invoice."""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPreliminaryPdfDetailed', id=identifier)
        return data

    def getXlsFilename(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Billing_Invoice', 'getXlsFilename', id=identifier)
        return data

    def getZeroFeeItemCounts(self, identifier: int) -> list['Container_Product_Item_Category_ZeroFee_Count']:
        data = self.client.call('SoftLayer_Billing_Invoice', 'getZeroFeeItemCounts', id=identifier)
        from SoftLayer.sltypes.Container_Product_Item_Category_ZeroFee_Count import Container_Product_Item_Category_ZeroFee_Count
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getAmount', id=identifier)
        return data

    def getBrandAtInvoiceCreation(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getBrandAtInvoiceCreation', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getChargebackType(self, identifier: int) -> 'Billing_Chargeback_Type':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getChargebackType', id=identifier)
        from SoftLayer.sltypes.Billing_Chargeback_Type import Billing_Chargeback_Type
        return data

    def getDetailedPdfGeneratedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getDetailedPdfGeneratedFlag', id=identifier)
        return data

    def getInvoiceTopLevelItems(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTopLevelItems', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getInvoiceTotalAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalAmount', id=identifier)
        return data

    def getInvoiceTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalOneTimeAmount', id=identifier)
        return data

    def getInvoiceTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalOneTimeTaxAmount', id=identifier)
        return data

    def getInvoiceTotalPreTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalPreTaxAmount', id=identifier)
        return data

    def getInvoiceTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalRecurringAmount', id=identifier)
        return data

    def getInvoiceTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getInvoiceTotalRecurringTaxAmount', id=identifier)
        return data

    def getItems(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getItems', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getLocalCurrencyExchangeRate(self, identifier: int) -> 'Billing_Currency_ExchangeRate':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getLocalCurrencyExchangeRate', id=identifier)
        from SoftLayer.sltypes.Billing_Currency_ExchangeRate import Billing_Currency_ExchangeRate
        return data

    def getPayment(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPayment', id=identifier)
        return data

    def getPayments(self, identifier: int) -> list['Billing_Invoice_Receivable_Payment']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getPayments', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Receivable_Payment import Billing_Invoice_Receivable_Payment
        return data

    def getSellerRegistration(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getSellerRegistration', id=identifier)
        return data

    def getTaxInfo(self, identifier: int) -> 'Billing_Invoice_Tax_Info':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getTaxInfo', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Tax_Info import Billing_Invoice_Tax_Info
        return data

    def getTaxInfoHistory(self, identifier: int) -> list['Billing_Invoice_Tax_Info']:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getTaxInfoHistory', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Tax_Info import Billing_Invoice_Tax_Info
        return data

    def getTaxMessage(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getTaxMessage', id=identifier)
        return data

    def getTaxType(self, identifier: int) -> 'Billing_Invoice_Tax_Type':
        """"""
        data = self.client.call('SoftLayer_Billing_Invoice', 'getTaxType', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Tax_Type import Billing_Invoice_Tax_Type
        return data
