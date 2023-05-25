from datetime import datetime
from SoftLayer.sltypes.Billing.Payment.Transaction import Billing_Payment_Transaction
from SoftLayer.sltypes.Billing_Payment_Transaction import Billing_Payment_Transaction

class Billing_Payment_PayPal_Transaction(Billing_Payment_Transaction):
    """The SoftLayer_Billing_Payment_PayPal_Transaction data type contains general information relating to attempted
PayPal transactions."""
    accountId: int
    addressCityName: str
    addressCountry: str
    addressName: str
    addressPostalCode: str
    addressStateProvence: str
    addressStatus: str
    addressStreet1: str
    addressStreet2: str
    contactPhone: str
    createDate: datetime
    exchangeRate: str
    feeAmount: float
    grossAmount: float
    id_: int
    invoiceId: int
    lastPaypalCommand: str
    modifyDate: datetime
    orderFromIpAddress: str
    orderTotal: float
    payer: str
    payerBusiness: str
    payerCountry: str
    payerFirstName: str
    payerId: str
    payerLastName: str
    payerStatus: str
    paymentDate: datetime
    paymentStatus: str
    paymentType: str
    pendingReason: str
    serializedReply: str
    serializedRequest: str
    settleAmount: float
    taxAmount: float
    token: str
    transactionId: str
    transactionType: str
