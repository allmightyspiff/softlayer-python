# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service'
        self.client = client

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


    def getGraphImage(
        self,
        graphType: str,
        metric: str,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getGraphImage',
            graphType,
            metric,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service import Service
        return Service(data)


    def toggleStatus(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'toggleStatus',
            id=identifier
        )
        
        return data


    def getGroupReferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference]':

        data = self.client.call(
            self.service,
            'getGroupReferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group.CrossReference import CrossReference
        return CrossReference(data)


    def getGroups(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group]':

        data = self.client.call(
            self.service,
            'getGroups',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


    def getHealthCheck(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check':

        data = self.client.call(
            self.service,
            'getHealthCheck',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Health.Check import Check
        return Check(data)


    def getHealthChecks(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check]':

        data = self.client.call(
            self.service,
            'getHealthChecks',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Health.Check import Check
        return Check(data)


    def getIpAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getIpAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getServiceGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group':

        data = self.client.call(
            self.service,
            'getServiceGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


