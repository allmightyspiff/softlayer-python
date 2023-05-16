# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Workload_Citrix_Deployment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Workload_Citrix_Deployment'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Workload_Citrix_Deployment,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment import Deployment
        return Deployment(data)


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Workload_Citrix_Deployment]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment import Deployment
        return Deployment(data)


    def getDeployment(
        self,
        deploymentId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Response':

        data = self.client.call(
            self.service,
            'getDeployment',
            deploymentId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Response import Response
        return Response(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment import Deployment
        return Deployment(data)


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
        return Account(data)


    def getResources(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Workload_Citrix_Deployment_Resource]':

        data = self.client.call(
            self.service,
            'getResources',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Resource import Resource
        return Resource(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Status import Status
        return Status(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Type import Type
        return Type(data)


    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getVlan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Vlan':

        data = self.client.call(
            self.service,
            'getVlan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


