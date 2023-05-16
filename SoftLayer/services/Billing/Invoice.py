# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Invoice(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Invoice'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getExcel(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getExcel',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Invoice(data)

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
    def getPdfDetailed(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPdfDetailed',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPdfDetailedFilename(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPdfDetailedFilename',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPdfFileSize(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getPdfFileSize',
            
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
    def getPreliminaryExcel(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPreliminaryExcel',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPreliminaryPdf(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPreliminaryPdf',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPreliminaryPdfDetailed(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getPreliminaryPdfDetailed',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getXlsFilename(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getXlsFilename',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getZeroFeeItemCounts(
        self,
        
    ) -> 'list[SoftLayer_Container_Product_Item_Category_ZeroFee_Count]':
        data = self.client.call(
            self.service,
            'getZeroFeeItemCounts',
            
        )
        from SoftLayer.datatypes.Container.Product.Item.Category.ZeroFee.Count import Count
        return SL_Count(data)

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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ExchangeRate(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Payment(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Info(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Info(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)


