from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Internal_Ibm(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Internal_Ibm'

    def getAccountTypes(self) -> list[str]:
        """Retrieves allowed internal IBM account categories"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getAccountTypes')
        return data

    def getAuthorizationUrl(self, requestId: int) -> str:
        """Gets the redirect URL for manager validation"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getAuthorizationUrl', requestId)
        return data

    def getBmsCountries(self) -> list['BMS_Container_Country']:
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getBmsCountries')
        return data

    def getBmsCountryList(self) -> list[str]:
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getBmsCountryList')
        return data

    def getEmployeeAccessToken(self, unverifiedAuthenticationCode: str) -> str:
        """Exchanges a token"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getEmployeeAccessToken', unverifiedAuthenticationCode)
        return data

    def getManagerPreview(self, requestId: int, accessToken: str) -> 'Container_Account_Internal_Ibm_Request':
        """Gets a container representing the pending request"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'getManagerPreview', requestId, accessToken)
        from SoftLayer.sltypes.Container_Account_Internal_Ibm_Request import Container_Account_Internal_Ibm_Request
        return data

    def hasExistingRequest(self, employeeUid: str, managerUid: str) -> bool:
        """Checks for an existing request which would block an IBMer application"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'hasExistingRequest', employeeUid, managerUid)
        return data

    def managerApprove(self, requestId: int, accessToken: str) -> None:
        """Applies manager approval to a pending internal IBM account request"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'managerApprove', requestId, accessToken)
        return data

    def managerDeny(self, requestId: int, accessToken: str) -> None:
        """Applies manager denial to a pending request"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'managerDeny', requestId, accessToken)
        return data

    def requestAccount(self, requestContainer: 'Container_Account_Internal_Ibm_Request') -> None:
        """Processes IBMer requests for new IaaS/PaaS accounts"""
        data = self.client.call('SoftLayer_Account_Internal_Ibm', 'requestAccount', requestContainer)
        return data
