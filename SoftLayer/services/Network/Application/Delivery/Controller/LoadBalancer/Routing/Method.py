# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Routing.Method import Method
        return Method(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Method':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.Routing.Method import Method
        return Method(data)


