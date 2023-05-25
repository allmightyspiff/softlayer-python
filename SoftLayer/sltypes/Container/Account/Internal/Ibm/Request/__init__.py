from SoftLayer.sltypes.Entity import Entity

class Container_Account_Internal_Ibm_Request(Entity):
    """Contains data required to both request a new IaaS account for active IBM employees and review pending
requests. Fields used exclusively in the review process are scrubbed of user input."""
    accountType: str
    address1: str
    address2: str
    city: str
    companyName: str
    costRecoveryAccountId: str
    costRecoveryCountryId: str
    country: str
    deniedFlag: bool
    departmentCode: str
    departmentCountry: str
    divisionCode: str
    emailAddress: str
    firstName: str
    lastName: str
    managerApprovalStatus: str
    multiTenantFlag: bool
    officePhone: str
    paasAccountId: str
    postalCode: str
    purpose: str
    securitySubjectMatterExpertEmail: str
    securitySubjectMatterExpertName: str
    securitySubjectMatterExpertPhone: str
    state: str
