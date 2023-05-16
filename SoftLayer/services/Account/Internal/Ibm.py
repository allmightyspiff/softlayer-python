# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Internal_Ibm(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Internal_Ibm'
        self.client = client

    def getAccountTypes(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getAccountTypes',
            
        )
        
        return data


    def getAuthorizationUrl(
        self,
        requestId: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAuthorizationUrl',
            requestId
        )
        
        return data


    def getBmsCountries(
        self,
        
    ) -> 'list[BMS_Container_Country]':

        data = self.client.call(
            self.service,
            'getBmsCountries',
            
        )
        
        return data


    def getBmsCountryList(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getBmsCountryList',
            
        )
        
        return data


    def getEmployeeAccessToken(
        self,
        unverifiedAuthenticationCode: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getEmployeeAccessToken',
            unverifiedAuthenticationCode
        )
        
        return data


    def getManagerPreview(
        self,
        requestId: int,
        accessToken: str
    ) -> 'SoftLayer_Container_Account_Internal_Ibm_Request':

        data = self.client.call(
            self.service,
            'getManagerPreview',
            requestId,
            accessToken
        )
        from SoftLayer.datatypes.Container.Account.Internal.Ibm.Request import Request
        return Request(data)


    def hasExistingRequest(
        self,
        employeeUid: str,
        managerUid: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'hasExistingRequest',
            employeeUid,
            managerUid
        )
        
        return data


    def managerApprove(
        self,
        requestId: int,
        accessToken: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'managerApprove',
            requestId,
            accessToken
        )
        
        return data


    def managerDeny(
        self,
        requestId: int,
        accessToken: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'managerDeny',
            requestId,
            accessToken
        )
        
        return data


    def requestAccount(
        self,
        requestContainer: SoftLayer_Container_Account_Internal_Ibm_Request
    ) -> 'void':

        data = self.client.call(
            self.service,
            'requestAccount',
            requestContainer
        )
        
        return data


