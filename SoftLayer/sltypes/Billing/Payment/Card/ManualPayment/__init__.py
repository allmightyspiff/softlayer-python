from SoftLayer.sltypes.Entity import Entity

class Billing_Payment_Card_ManualPayment(Entity):
    """The SoftLayer_Billing_Payment_Card_ManualPayment data type contains general information related to requesting
a manual payment. This supports enablement of 3D Secure via Cardinal Cruise implementation that allows for
credit card authentication and is currently limited to specified merchants."""
    accountId: int
    amount: float
    authorizedCreditCardTransactionId: int
    authorizedPayPalTransactionId: int
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
    cancelUrl: str
    cardAccountHash: str
    cardAccountLast4: str
    cardAccountNumber: str
    cardExpirationMonth: str
    cardExpirationYear: str
    cardType: str
    creditCardVerificationNumber: str
    currencyShortName: str
    deviceFingerprintId: str
    fromIpAddress: str
    id_: int
    notes: str
    payerAuthenticationEnrollmentReferenceId: str
    payerAuthenticationEnrollmentReturnUrl: str
    payerAuthenticationWebToken: str
    paymentType: str
    returnUrl: str
    type_: str
