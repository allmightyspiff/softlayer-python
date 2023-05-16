# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Workload_Citrix_Deployment_Resource(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Workload_Citrix_Deployment_Resource'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Workload_Citrix_Deployment_Resource,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Resource':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Resource import Resource
        return Resource(data)


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Workload_Citrix_Deployment_Resource]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Resource import Resource
        return Resource(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Resource':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Resource import Resource
        return Resource(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getDeployment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment':

        data = self.client.call(
            self.service,
            'getDeployment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment import Deployment
        return Deployment(data)


    def getOrder(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':

        data = self.client.call(
            self.service,
            'getOrder',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


    def getRole(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Resource_Role':

        data = self.client.call(
            self.service,
            'getRole',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Resource.Role import Role
        return Role(data)


