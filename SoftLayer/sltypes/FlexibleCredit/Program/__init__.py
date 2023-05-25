from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class FlexibleCredit_Program(Entity):
    id_: int
    keyName: str
    name: str
    platformPromotionCode: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_FlexibleCredit_Program'

    def getAffiliatesAvailableForSelfEnrollmentByVerificationType(self, identifier: int, verificationTypeKeyName: str) -> list['FlexibleCredit_Affiliate']:
        data = self.client.call('SoftLayer_FlexibleCredit_Program', 'getAffiliatesAvailableForSelfEnrollmentByVerificationType', verificationTypeKeyName, id=identifier)
        from SoftLayer.sltypes.FlexibleCredit_Affiliate import FlexibleCredit_Affiliate
        return data

    def getCompanyTypes(self) -> list['FlexibleCredit_Company_Type']:
        data = self.client.call('SoftLayer_FlexibleCredit_Program', 'getCompanyTypes')
        from SoftLayer.sltypes.FlexibleCredit_Company_Type import FlexibleCredit_Company_Type
        return data

    def getObject(self, identifier: int) -> 'FlexibleCredit_Program':
        """Retrieve a SoftLayer_FlexibleCredit_Program record."""
        data = self.client.call('SoftLayer_FlexibleCredit_Program', 'getObject', id=identifier)
        return data

    def selfEnrollNewAccount(self, identifier: int, accountTemplate: 'Account') -> 'Account':
        data = self.client.call('SoftLayer_FlexibleCredit_Program', 'selfEnrollNewAccount', accountTemplate, id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data
