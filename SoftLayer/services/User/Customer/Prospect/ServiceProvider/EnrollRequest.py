# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest'
        self.client = client

    def enroll(
        self,
        templateObject: SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest':

        data = self.client.call(
            self.service,
            'enroll',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Prospect.ServiceProvider.EnrollRequest import EnrollRequest
        return EnrollRequest(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Prospect_ServiceProvider_EnrollRequest':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Prospect.ServiceProvider.EnrollRequest import EnrollRequest
        return EnrollRequest(data)


    def getCompanyType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Catalyst_Company_Type':

        data = self.client.call(
            self.service,
            'getCompanyType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Catalyst.Company.Type import Type
        return Type(data)


