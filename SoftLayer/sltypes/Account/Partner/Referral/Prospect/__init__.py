from SoftLayer.sltypes.User.Customer.Prospect import User_Customer_Prospect
from SoftLayer.sltypes.User_Customer_Prospect import User_Customer_Prospect
from SoftLayer import BaseClient

class Account_Partner_Referral_Prospect(User_Customer_Prospect):
    companyName: str
    emailAddress: str
    firstName: str
    id_: int
    lastName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Partner_Referral_Prospect'

    def createProspect(self, templateObject: 'Container_Referral_Partner_Prospect', commit: bool) -> 'Account_Partner_Referral_Prospect':
        """Creates a new Referral Partner Prospect"""
        data = self.client.call('SoftLayer_Account_Partner_Referral_Prospect', 'createProspect', templateObject, commit)
        return data

    def getObject(self, identifier: int) -> 'Account_Partner_Referral_Prospect':
        """Retrieve a SoftLayer_Account_Partner_Referral_Prospect record."""
        data = self.client.call('SoftLayer_Account_Partner_Referral_Prospect', 'getObject', id=identifier)
        return data

    def getSurveyQuestions(self) -> list['Survey_Question']:
        """Retrieves Questions for a Referral Partner Survey"""
        data = self.client.call('SoftLayer_Account_Partner_Referral_Prospect', 'getSurveyQuestions')
        from SoftLayer.sltypes.Survey_Question import Survey_Question
        return data
