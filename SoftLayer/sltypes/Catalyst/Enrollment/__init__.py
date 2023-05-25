from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Catalyst_Enrollment(Entity):
    accountId: int
    affiliateId: int
    agreementCompleteFlag: int
    companyDescription: str
    companyTypeId: int
    enrollmentDate: datetime
    graduationDate: datetime
    monthlyCreditAmount: float
    representativeEmployeeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Catalyst_Enrollment'

    def getAffiliates(self) -> list['Catalyst_Affiliate']:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getAffiliates')
        from SoftLayer.sltypes.Catalyst_Affiliate import Catalyst_Affiliate
        return data

    def getCompanyTypes(self) -> list['Catalyst_Company_Type']:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getCompanyTypes')
        from SoftLayer.sltypes.Catalyst_Company_Type import Catalyst_Company_Type
        return data

    def getEnrollmentRequestAnnualRevenueOptions(self) -> list['Catalyst_Enrollment_Request_Container_AnswerOption']:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getEnrollmentRequestAnnualRevenueOptions')
        from SoftLayer.sltypes.Catalyst_Enrollment_Request_Container_AnswerOption import Catalyst_Enrollment_Request_Container_AnswerOption
        return data

    def getEnrollmentRequestUserCountOptions(self) -> list['Catalyst_Enrollment_Request_Container_AnswerOption']:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getEnrollmentRequestUserCountOptions')
        from SoftLayer.sltypes.Catalyst_Enrollment_Request_Container_AnswerOption import Catalyst_Enrollment_Request_Container_AnswerOption
        return data

    def getEnrollmentRequestYearsInOperationOptions(self) -> list['Catalyst_Enrollment_Request_Container_AnswerOption']:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getEnrollmentRequestYearsInOperationOptions')
        from SoftLayer.sltypes.Catalyst_Enrollment_Request_Container_AnswerOption import Catalyst_Enrollment_Request_Container_AnswerOption
        return data

    def getObject(self, identifier: int) -> 'Catalyst_Enrollment':
        """Retrieve a SoftLayer_Catalyst_Enrollment record."""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getObject', id=identifier)
        return data

    def requestManualEnrollment(self, request: 'Container_Catalyst_ManualEnrollmentRequest') -> None:
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'requestManualEnrollment', request)
        return data

    def requestSelfEnrollment(self, enrollmentRequest: 'Catalyst_Enrollment_Request') -> 'Account':
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'requestSelfEnrollment', enrollmentRequest)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAffiliate(self, identifier: int) -> 'Catalyst_Affiliate':
        """"""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getAffiliate', id=identifier)
        from SoftLayer.sltypes.Catalyst_Affiliate import Catalyst_Affiliate
        return data

    def getCompanyType(self, identifier: int) -> 'Catalyst_Company_Type':
        """"""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getCompanyType', id=identifier)
        from SoftLayer.sltypes.Catalyst_Company_Type import Catalyst_Company_Type
        return data

    def getIsActiveFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getIsActiveFlag', id=identifier)
        return data

    def getRepresentative(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Catalyst_Enrollment', 'getRepresentative', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data
