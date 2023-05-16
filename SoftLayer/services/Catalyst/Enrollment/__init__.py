# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Catalyst_Enrollment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Catalyst_Enrollment'
        self.client = client

    def getAffiliates(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Catalyst_Affiliate]':

        data = self.client.call(
            self.service,
            'getAffiliates',
            mask=objectMask
        )
        from SoftLayer.datatypes.Catalyst.Affiliate import Affiliate
        return Affiliate(data)


    def getCompanyTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Catalyst_Company_Type]':

        data = self.client.call(
            self.service,
            'getCompanyTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Catalyst.Company.Type import Type
        return Type(data)


    def getEnrollmentRequestAnnualRevenueOptions(
        self,
        
    ) -> 'list[SoftLayer_Catalyst_Enrollment_Request_Container_AnswerOption]':

        data = self.client.call(
            self.service,
            'getEnrollmentRequestAnnualRevenueOptions',
            
        )
        from SoftLayer.datatypes.Catalyst.Enrollment.Request.Container.AnswerOption import AnswerOption
        return AnswerOption(data)


    def getEnrollmentRequestUserCountOptions(
        self,
        
    ) -> 'list[SoftLayer_Catalyst_Enrollment_Request_Container_AnswerOption]':

        data = self.client.call(
            self.service,
            'getEnrollmentRequestUserCountOptions',
            
        )
        from SoftLayer.datatypes.Catalyst.Enrollment.Request.Container.AnswerOption import AnswerOption
        return AnswerOption(data)


    def getEnrollmentRequestYearsInOperationOptions(
        self,
        
    ) -> 'list[SoftLayer_Catalyst_Enrollment_Request_Container_AnswerOption]':

        data = self.client.call(
            self.service,
            'getEnrollmentRequestYearsInOperationOptions',
            
        )
        from SoftLayer.datatypes.Catalyst.Enrollment.Request.Container.AnswerOption import AnswerOption
        return AnswerOption(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Catalyst_Enrollment':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Catalyst.Enrollment import Enrollment
        return Enrollment(data)


    def requestManualEnrollment(
        self,
        request: 'SoftLayer_Container_Catalyst_ManualEnrollmentRequest'
    ) -> 'void':

        data = self.client.call(
            self.service,
            'requestManualEnrollment',
            request
        )
        
        return data


    def requestSelfEnrollment(
        self,
        enrollmentRequest: 'SoftLayer_Catalyst_Enrollment_Request',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'requestSelfEnrollment',
            enrollmentRequest,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getAffiliate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Catalyst_Affiliate':

        data = self.client.call(
            self.service,
            'getAffiliate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Catalyst.Affiliate import Affiliate
        return Affiliate(data)


    def getCompanyType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Catalyst_Company_Type':

        data = self.client.call(
            self.service,
            'getCompanyType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Catalyst.Company.Type import Type
        return Type(data)


    def getIsActiveFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsActiveFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRepresentative(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getRepresentative',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


