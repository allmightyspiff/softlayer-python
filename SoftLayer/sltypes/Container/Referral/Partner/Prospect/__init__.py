from SoftLayer.sltypes.Survey.Response import Survey_Response
from SoftLayer.sltypes.Entity import Entity

class Container_Referral_Partner_Prospect(Entity):
    address1: str
    address2: str
    city: str
    companyName: str
    country: str
    email: str
    firstName: str
    lastName: str
    officePhone: str
    postalCode: str
    questions: list[str]
    responses: list[Survey_Response]
    state: str
    surveyId: str
