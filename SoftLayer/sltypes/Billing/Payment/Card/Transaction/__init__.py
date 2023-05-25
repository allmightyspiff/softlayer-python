from datetime import datetime
from SoftLayer.sltypes.Billing.Payment.Transaction import Billing_Payment_Transaction
from SoftLayer.sltypes.Billing_Payment_Transaction import Billing_Payment_Transaction

class Billing_Payment_Card_Transaction(Billing_Payment_Transaction):
    """The SoftLayer_Billing_Payment_Card_Transaction data type contains general information relating to attempted
credit card transactions."""
    accountId: int
    amount: float
    billingAddressLine1: str
    billingAddressLine2: str
    billingCity: str
    billingCountryCode: str
    billingEmail: str
    billingNameCompany: str
    billingNameFirst: str
    billingNameLast: str
    billingPhoneFax: str
    billingPhoneVoice: str
    billingPostalCode: str
    billingState: str
    cardAccountLast4: int
    cardExpirationMonth: int
    cardExpirationYear: int
    cardType: str
    createDate: datetime
    id_: int
    invoiceId: int
    modifyDate: datetime
    orderFromIpAddress: str
    referenceCode: str
    requestId: str
    returnStatus: int
    serializedReply: str
    serializedRequest: str
