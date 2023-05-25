from SoftLayer.sltypes.Survey.Response import Survey_Response
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Prospect_ServiceProvider_EnrollRequest(Entity):
    """Contains user information for Service Provider Enrollment."""
    acceptAllAgreementsFlag: bool
    accountId: int
    address1: str
    address2: str
    cardAccountNumber: str
    cardExpirationMonth: str
    cardExpirationYear: str
    cardType: str
    cardVerificationNumber: str
    city: str
    companyName: str
    companyTypeId: int
    companyUrl: str
    contactEmail: str
    contactFirstName: str
    contactLastName: str
    contactPhone: str
    country: str
    customerProspectId: int
    deviceFingerprintId: str
    email: str
    existingCustomerFlag: bool
    firstName: str
    ibmIdUsername: str
    ibmPartnerWorldId: str
    ibmPartnerWorldMemberFlag: bool
    lastName: str
    masterAgreementCompleteFlag: bool
    officePhone: str
    postalCode: str
    serviceProviderAddendumFlag: bool
    state: str
    surveyResponses: list[Survey_Response]
    vatId: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest'

    def enroll(self, templateObject: 'User_Customer_Prospect_ServiceProvider_EnrollRequest') -> 'User_Customer_Prospect_ServiceProvider_EnrollRequest':
        """Creates a new Service Provider Enrollment"""
        data = self.client.call('SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest', 'enroll', templateObject)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_Prospect_ServiceProvider_EnrollRequest':
        """Retrieve a SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest record."""
        data = self.client.call('SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest', 'getObject', id=identifier)
        return data

    def getCompanyType(self, identifier: int) -> 'Catalyst_Company_Type':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest', 'getCompanyType', id=identifier)
        from SoftLayer.sltypes.Catalyst_Company_Type import Catalyst_Company_Type
        return data
