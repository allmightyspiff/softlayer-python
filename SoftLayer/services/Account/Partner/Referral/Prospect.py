# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Partner_Referral_Prospect(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Partner_Referral_Prospect'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createProspect(
        self,
        templateObject: SoftLayer_Container_Referral_Partner_Prospect,
        commit: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Partner_Referral_Prospect':
        data = self.client.call(
            self.service,
            'createProspect',
            templateObject,
            commit,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Partner.Referral.Prospect import Prospect
        return SL_Prospect(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Partner_Referral_Prospect':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Partner.Referral.Prospect import Prospect
        return SL_Prospect(data)

# This file was automatically generated with tools/generateTypes.py
    def getSurveyQuestions(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Survey_Question]':
        data = self.client.call(
            self.service,
            'getSurveyQuestions',
            mask=objectMask
        )
        from SoftLayer.datatypes.Survey.Question import Question
        return SL_Question(data)

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getAssignedEmployees(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Employee]':
        data = self.client.call(
            self.service,
            'getAssignedEmployees',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return SL_Employee(data)

# This file was automatically generated with tools/generateTypes.py
    def getQuotes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Quote]':
        data = self.client.call(
            self.service,
            'getQuotes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return SL_Quote(data)

# This file was automatically generated with tools/generateTypes.py
    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Prospect_Type':
        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Prospect.Type import Type
        return SL_Type(data)


