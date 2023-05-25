from SoftLayer.sltypes.Entity import Entity

class Catalyst_Enrollment_Request(Entity):
    """Contains user information for Catalyst self-enrollment."""
    address1: str
    address2: str
    affiliateId: int
    agreementCompleteFlag: bool
    applyToGepFlag: bool
    cardAccountNumber: str
    cardExpirationMonth: str
    cardExpirationYear: str
    cardType: str
    cardVerificationNumber: str
    city: str
    companyDescription: str
    companyName: str
    companyTypeId: int
    companyUrl: str
    country: str
    currentUserChoice: int
    deviceFingerprintId: str
    email: str
    firstName: str
    futureUserChoice: int
    ibmIdUsername: str
    incubatorName: str
    investorName: str
    lastName: str
    officePhone: str
    overFiveYearsOldFlag: bool
    postalCode: str
    referralCode: str
    revenueOverOneMillionFlag: bool
    skipCatalystApplicationFlag: bool
    state: str
    vatId: str
