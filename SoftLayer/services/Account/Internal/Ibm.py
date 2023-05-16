# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Internal_Ibm(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Internal_Ibm'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAccountTypes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAccountTypes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getBmsCountries(
        self,
        
    ) -> 'list[BMS_Container_Country]':
        data = self.client.call(
            self.service,
            'getBmsCountries',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBmsCountryList(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getBmsCountryList',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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


