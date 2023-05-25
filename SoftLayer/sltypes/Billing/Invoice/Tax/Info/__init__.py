from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Invoice_Tax_Info(Entity):
    """Invoice tax information contains top-level information about the taxes recorded for a particular invoice."""
    createDate: datetime
    currencyId: int
    id_: int
    invoiceId: int
    modifyDate: datetime
    reportedFlag: bool
