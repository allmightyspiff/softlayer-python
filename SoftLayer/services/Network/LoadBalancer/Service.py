# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LoadBalancer_Service(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LoadBalancer_Service'
        self.client = client
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

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_Service':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Service import Service
        return SL_Service(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_LoadBalancer_StatusEntry]':
        data = self.client.call(
            self.service,
            'getStatus',
            
        )
        from SoftLayer.datatypes.Container.Network.LoadBalancer.StatusEntry import StatusEntry
        return SL_StatusEntry(data)

# This file was automatically generated with tools/generateTypes.py
    def resetPeakConnections(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'resetPeakConnections',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getVip(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_VirtualIpAddress':
        data = self.client.call(
            self.service,
            'getVip',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return SL_VirtualIpAddress(data)


