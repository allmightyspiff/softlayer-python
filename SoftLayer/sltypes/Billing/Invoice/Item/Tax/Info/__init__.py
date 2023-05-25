from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Invoice_Item_Tax_Info(Entity):
    """Information about the tax rates that apply to a particular invoice item."""
    createDate: datetime
    description: str
    effectiveTaxRate: float
    exemptAmount: float
    feeProperty: str
    id_: int
    invoiceItemId: int
    invoiceTaxInfoId: int
    modifyDate: datetime
    nonTaxableBasis: float
    reportedFlag: bool
    sellerRegistration: str
    taxAmount: float
    taxAmountToCurrency: float
    taxRate: float
    taxableBasis: float
    toCurrencyId: int
