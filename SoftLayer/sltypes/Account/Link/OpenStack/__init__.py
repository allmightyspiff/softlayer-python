from SoftLayer.sltypes.Account.Link import Account_Link
from SoftLayer.sltypes.Account_Link import Account_Link
from SoftLayer import BaseClient

class Account_Link_OpenStack(Account_Link):
    domainId: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Link_OpenStack'

    def createOSDomain(self, request: 'Account_Link_OpenStack_LinkRequest') -> 'Account_Link_OpenStack_DomainCreationDetails':
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'createOSDomain', request)
        from SoftLayer.sltypes.Account_Link_OpenStack_DomainCreationDetails import Account_Link_OpenStack_DomainCreationDetails
        return data

    def createOSProject(self, request: 'Account_Link_OpenStack_LinkRequest') -> 'Account_Link_OpenStack_ProjectCreationDetails':
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'createOSProject', request)
        from SoftLayer.sltypes.Account_Link_OpenStack_ProjectCreationDetails import Account_Link_OpenStack_ProjectCreationDetails
        return data

    def deleteOSDomain(self, domainId: str) -> bool:
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'deleteOSDomain', domainId)
        return data

    def deleteOSProject(self, projectId: str) -> bool:
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'deleteOSProject', projectId)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Remove an account link."""
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'deleteObject', id=identifier)
        return data

    def getOSProject(self, projectId: str) -> 'Account_Link_OpenStack_ProjectDetails':
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'getOSProject', projectId)
        from SoftLayer.sltypes.Account_Link_OpenStack_ProjectDetails import Account_Link_OpenStack_ProjectDetails
        return data

    def getObject(self, identifier: int) -> 'Account_Link_OpenStack':
        """Retrieve a SoftLayer_Account_Link_OpenStack record."""
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'getObject', id=identifier)
        return data

    def listOSProjects(self) -> list['Account_Link_OpenStack_ProjectDetails']:
        data = self.client.call('SoftLayer_Account_Link_OpenStack', 'listOSProjects')
        from SoftLayer.sltypes.Account_Link_OpenStack_ProjectDetails import Account_Link_OpenStack_ProjectDetails
        return data
