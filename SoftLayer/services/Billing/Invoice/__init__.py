# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Invoice(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Invoice'
        self.client = client

    def emailInvoices(
        self,
        options: 'SoftLayer_Container_Billing_Invoice_Email'
    ) -> 'void':

        data = self.client.call(
            self.service,
            'emailInvoices',
            options
        )
        
        return data


    def getExcel(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getExcel',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


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


    def getPdfDetailed(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdfDetailed',
            id=identifier
        )
        
        return data


    def getPdfDetailedFilename(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPdfDetailedFilename',
            id=identifier
        )
        
        return data


    def getPdfFileSize(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getPdfFileSize',
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


    def getPreliminaryExcel(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryExcel',
            id=identifier
        )
        
        return data


    def getPreliminaryPdf(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryPdf',
            id=identifier
        )
        
        return data


    def getPreliminaryPdfDetailed(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryPdfDetailed',
            id=identifier
        )
        
        return data


    def getXlsFilename(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getXlsFilename',
            id=identifier
        )
        
        return data


    def getZeroFeeItemCounts(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Product_Item_Category_ZeroFee_Count]':

        data = self.client.call(
            self.service,
            'getZeroFeeItemCounts',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Product.Item.Category.ZeroFee.Count import Count
        return Count(data)


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


    def getAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBrandAtInvoiceCreation(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getBrandAtInvoiceCreation',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getChargebackType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Chargeback_Type':

        data = self.client.call(
            self.service,
            'getChargebackType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Chargeback.Type import Type
        return Type(data)


    def getDetailedPdfGeneratedFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDetailedPdfGeneratedFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTopLevelItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':

        data = self.client.call(
            self.service,
            'getInvoiceTopLevelItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return Item(data)


    def getInvoiceTotalAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalOneTimeAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalOneTimeAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalOneTimeTaxAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalOneTimeTaxAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalPreTaxAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalPreTaxAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalRecurringAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalRecurringAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalRecurringTaxAmount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalRecurringTaxAmount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':

        data = self.client.call(
            self.service,
            'getItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return Item(data)


    def getLocalCurrencyExchangeRate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':

        data = self.client.call(
            self.service,
            'getLocalCurrencyExchangeRate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


    def getPayment(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPayment',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPayments(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Receivable_Payment]':

        data = self.client.call(
            self.service,
            'getPayments',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Receivable.Payment import Payment
        return Payment(data)


    def getSellerRegistration(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSellerRegistration',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTaxInfo(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice_Tax_Info':

        data = self.client.call(
            self.service,
            'getTaxInfo',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Info import Info
        return Info(data)


    def getTaxInfoHistory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Tax_Info]':

        data = self.client.call(
            self.service,
            'getTaxInfoHistory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Info import Info
        return Info(data)


    def getTaxMessage(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTaxMessage',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTaxType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice_Tax_Type':

        data = self.client.call(
            self.service,
            'getTaxType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Type import Type
        return Type(data)


