from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_Billing_Information(Entity):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order with SoftLayer."""
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
    cardAccountNumber: str
    cardExpirationMonth: int
    cardExpirationYear: int
    creditCardVerificationNumber: str
    euSupported: bool
    isBusinessFlag: bool
    payerAuthenticationEnrollmentReferenceId: str
    payerAuthenticationEnrollmentReturnUrl: str
    payerAuthenticationWebToken: str
    taxExempt: int
    vatId: str
