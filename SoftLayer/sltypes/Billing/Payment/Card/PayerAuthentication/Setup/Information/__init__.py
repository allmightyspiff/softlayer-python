from SoftLayer.sltypes.Entity import Entity

class Billing_Payment_Card_PayerAuthentication_Setup_Information(Entity):
    """This is the datatype that needs to be populated and sent to SoftLayer_Account::initiatePayerAuthentication."""
    billingAddressLine1: str
    billingAddressLine2: str
    billingCity: str
    billingCountryCode: str
    billingEmail: str
    billingNameFirst: str
    billingNameLast: str
    billingPostalCode: str
    billingState: str
    cardAccountNumber: str
    cardExpirationMonth: int
    cardExpirationYear: int
    cardType: str
    creditCardVerificationNumber: str
