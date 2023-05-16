# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service'
        self.client = client

    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def getGraphImage(
        self,
        graphType: str,
        metric: str
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getGraphImage',
            graphType,
            metric
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service import Service
        return Service(data)


    def toggleStatus(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'toggleStatus',
            
        )
        
        return data


    def getGroupReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference]':

        data = self.client.call(
            self.service,
            'getGroupReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group.CrossReference import CrossReference
        return CrossReference(data)


    def getGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group]':

        data = self.client.call(
            self.service,
            'getGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


    def getHealthCheck(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check':

        data = self.client.call(
            self.service,
            'getHealthCheck',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Health.Check import Check
        return Check(data)


    def getHealthChecks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check]':

        data = self.client.call(
            self.service,
            'getHealthChecks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Health.Check import Check
        return Check(data)


    def getIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getServiceGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group':

        data = self.client.call(
            self.service,
            'getServiceGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


