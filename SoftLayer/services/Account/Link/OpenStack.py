# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Link_OpenStack(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Link_OpenStack'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createOSDomain(
        self,
        request: SoftLayer_Account_Link_OpenStack_LinkRequest
    ) -> 'SoftLayer_Account_Link_OpenStack_DomainCreationDetails':
        data = self.client.call(
            self.service,
            'createOSDomain',
            request
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.DomainCreationDetails import DomainCreationDetails
        return SL_DomainCreationDetails(data)

# This file was automatically generated with tools/generateTypes.py
    def createOSProject(
        self,
        request: SoftLayer_Account_Link_OpenStack_LinkRequest
    ) -> 'SoftLayer_Account_Link_OpenStack_ProjectCreationDetails':
        data = self.client.call(
            self.service,
            'createOSProject',
            request
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.ProjectCreationDetails import ProjectCreationDetails
        return SL_ProjectCreationDetails(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteOSDomain(
        self,
        domainId: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteOSDomain',
            domainId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteOSProject(
        self,
        projectId: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteOSProject',
            projectId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOSProject(
        self,
        projectId: str
    ) -> 'SoftLayer_Account_Link_OpenStack_ProjectDetails':
        data = self.client.call(
            self.service,
            'getOSProject',
            projectId
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.ProjectDetails import ProjectDetails
        return SL_ProjectDetails(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Link_OpenStack':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Link.OpenStack import OpenStack
        return SL_OpenStack(data)

# This file was automatically generated with tools/generateTypes.py
    def listOSProjects(
        self,
        
    ) -> 'list[SoftLayer_Account_Link_OpenStack_ProjectDetails]':
        data = self.client.call(
            self.service,
            'listOSProjects',
            
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.ProjectDetails import ProjectDetails
        return SL_ProjectDetails(data)

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
    def getServiceProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':
        data = self.client.call(
            self.service,
            'getServiceProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return SL_Provider(data)


