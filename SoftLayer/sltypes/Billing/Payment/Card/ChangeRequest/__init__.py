from SoftLayer.sltypes.Entity import Entity

class Billing_Payment_Card_ChangeRequest(Entity):
    """The SoftLayer_Billing_Payment_Card_ChangeRequest data type contains general information relating to attempted
credit card information changes. This supports enablement of 3D Secure via Cardinal Cruise implementation
that allows for credit card authentication and is currently limited to specified merchants."""
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
    cardAccountLast4: str
    cardAccountNumber: str
    cardExpirationMonth: str
    cardExpirationYear: str
    cardNickname: str
    cardType: str
    creditCardVerificationNumber: str
    currencyShortName: str
    deviceFingerprintId: str
    id_: int
    notes: str
    payerAuthenticationEnrollmentReferenceId: str
    payerAuthenticationEnrollmentReturnUrl: str
    payerAuthenticationWebToken: str
    paymentRoleId: int
    paymentType: str
    ticketId: int
