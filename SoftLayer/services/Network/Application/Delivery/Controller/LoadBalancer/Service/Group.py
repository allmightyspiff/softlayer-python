# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'
        self.client = client

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
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


    def kickAllConnections(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'kickAllConnections',
            
        )
        
        return data


    def getRoutingMethod(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method':

        data = self.client.call(
            self.service,
            'getRoutingMethod',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Routing.Method import Method
        return Method(data)


    def getRoutingType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type':

        data = self.client.call(
            self.service,
            'getRoutingType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Routing.Type import Type
        return Type(data)


    def getServiceReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference]':

        data = self.client.call(
            self.service,
            'getServiceReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group.CrossReference import CrossReference
        return CrossReference(data)


    def getServices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service]':

        data = self.client.call(
            self.service,
            'getServices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service import Service
        return Service(data)


    def getVirtualServer(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer':

        data = self.client.call(
            self.service,
            'getVirtualServer',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualServer import VirtualServer
        return VirtualServer(data)


    def getVirtualServers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer]':

        data = self.client.call(
            self.service,
            'getVirtualServers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualServer import VirtualServer
        return VirtualServer(data)


