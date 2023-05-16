# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'
        self.client = client

    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualServer import VirtualServer
        return VirtualServer(data)


    def startSsl(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'startSsl',
            
        )
        
        return data


    def stopSsl(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'stopSsl',
            
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


    def getServiceGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group]':

        data = self.client.call(
            self.service,
            'getServiceGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Service.Group import Group
        return Group(data)


    def getVirtualIpAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress':

        data = self.client.call(
            self.service,
            'getVirtualIpAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


