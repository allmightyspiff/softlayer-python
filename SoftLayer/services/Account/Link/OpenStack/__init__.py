# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Link_OpenStack(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Link_OpenStack'
        self.client = client

    def createOSDomain(
        self,
        request: 'SoftLayer_Account_Link_OpenStack_LinkRequest'
    ) -> 'SoftLayer_Account_Link_OpenStack_DomainCreationDetails':

        data = self.client.call(
            self.service,
            'createOSDomain',
            request
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.DomainCreationDetails import DomainCreationDetails
        return DomainCreationDetails(data)


    def createOSProject(
        self,
        request: 'SoftLayer_Account_Link_OpenStack_LinkRequest'
    ) -> 'SoftLayer_Account_Link_OpenStack_ProjectCreationDetails':

        data = self.client.call(
            self.service,
            'createOSProject',
            request
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.ProjectCreationDetails import ProjectCreationDetails
        return ProjectCreationDetails(data)


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


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


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
        return ProjectDetails(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Link_OpenStack':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Link.OpenStack import OpenStack
        return OpenStack(data)


    def listOSProjects(
        self,
        
    ) -> 'list[SoftLayer_Account_Link_OpenStack_ProjectDetails]':

        data = self.client.call(
            self.service,
            'listOSProjects',
            
        )
        from SoftLayer.datatypes.Account.Link.OpenStack.ProjectDetails import ProjectDetails
        return ProjectDetails(data)


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


    def getServiceProvider(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':

        data = self.client.call(
            self.service,
            'getServiceProvider',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return Provider(data)


