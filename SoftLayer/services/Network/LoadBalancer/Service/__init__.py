# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LoadBalancer_Service(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LoadBalancer_Service'
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
    ) -> 'SoftLayer_Network_LoadBalancer_Service':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Service import Service
        return Service(data)


    def getStatus(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_LoadBalancer_StatusEntry]':

        data = self.client.call(
            self.service,
            'getStatus',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.LoadBalancer.StatusEntry import StatusEntry
        return StatusEntry(data)


    def resetPeakConnections(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'resetPeakConnections',
            id=identifier
        )
        
        return data


    def getVip(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_VirtualIpAddress':

        data = self.client.call(
            self.service,
            'getVip',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


