from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Invoice_Receivable_Payment(Entity):
    """The SoftLayer_Billing_Invoice_Receivable_Payment data type contains general information relating to payments
made against invoices."""
    amount: float
    createDate: datetime
    invoiceId: int
    typeCode: str
