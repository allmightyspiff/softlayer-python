# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Invoice(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Invoice'
        self.client = client

    def emailInvoices(
        self,
        options: SoftLayer_Container_Billing_Invoice_Email
    ) -> 'void':

        data = self.client.call(
            self.service,
            'emailInvoices',
            options
        )
        
        return data


    def getExcel(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getExcel',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getPdf(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdf',
            
        )
        
        return data


    def getPdfDetailed(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdfDetailed',
            
        )
        
        return data


    def getPdfDetailedFilename(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPdfDetailedFilename',
            
        )
        
        return data


    def getPdfFileSize(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getPdfFileSize',
            
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


    def getPreliminaryExcel(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryExcel',
            
        )
        
        return data


    def getPreliminaryPdf(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryPdf',
            
        )
        
        return data


    def getPreliminaryPdfDetailed(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPreliminaryPdfDetailed',
            
        )
        
        return data


    def getXlsFilename(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getXlsFilename',
            
        )
        
        return data


    def getZeroFeeItemCounts(
        self,
        
    ) -> 'list[SoftLayer_Container_Product_Item_Category_ZeroFee_Count]':

        data = self.client.call(
            self.service,
            'getZeroFeeItemCounts',
            
        )
        from SoftLayer.datatypes.Container.Product.Item.Category.ZeroFee.Count import Count
        return Count(data)


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


    def getAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBrandAtInvoiceCreation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getBrandAtInvoiceCreation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getChargebackType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Chargeback_Type':

        data = self.client.call(
            self.service,
            'getChargebackType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Chargeback.Type import Type
        return Type(data)


    def getDetailedPdfGeneratedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDetailedPdfGeneratedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTopLevelItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':

        data = self.client.call(
            self.service,
            'getInvoiceTopLevelItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return Item(data)


    def getInvoiceTotalAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalOneTimeAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalOneTimeAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalOneTimeTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalOneTimeTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalPreTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalPreTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalRecurringAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalRecurringAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoiceTotalRecurringTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getInvoiceTotalRecurringTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':

        data = self.client.call(
            self.service,
            'getItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return Item(data)


    def getLocalCurrencyExchangeRate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency_ExchangeRate':

        data = self.client.call(
            self.service,
            'getLocalCurrencyExchangeRate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency.ExchangeRate import ExchangeRate
        return ExchangeRate(data)


    def getPayment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPayment',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPayments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Receivable_Payment]':

        data = self.client.call(
            self.service,
            'getPayments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Receivable.Payment import Payment
        return Payment(data)


    def getSellerRegistration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSellerRegistration',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTaxInfo(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice_Tax_Info':

        data = self.client.call(
            self.service,
            'getTaxInfo',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Info import Info
        return Info(data)


    def getTaxInfoHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Tax_Info]':

        data = self.client.call(
            self.service,
            'getTaxInfoHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Info import Info
        return Info(data)


    def getTaxMessage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTaxMessage',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTaxType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice_Tax_Type':

        data = self.client.call(
            self.service,
            'getTaxType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice.Tax.Type import Type
        return Type(data)


