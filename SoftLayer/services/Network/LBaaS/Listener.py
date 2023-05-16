# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_Listener(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_Listener'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def deleteLoadBalancerProtocols(
        self,
        loadBalancerUuid: str,
        listenerUuids: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'deleteLoadBalancerProtocols',
            loadBalancerUuid,
            listenerUuids,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_Listener':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.Listener import Listener
        return SL_Listener(data)

# This file was automatically generated with tools/generateTypes.py
    def updateLoadBalancerProtocols(
        self,
        loadBalancerUuid: str,
        protocolConfigurations: SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'updateLoadBalancerProtocols',
            loadBalancerUuid,
            protocolConfigurations,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getDefaultPool(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_Pool':
        data = self.client.call(
            self.service,
            'getDefaultPool',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.Pool import Pool
        return SL_Pool(data)

# This file was automatically generated with tools/generateTypes.py
    def getL7Policies(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_L7Policy]':
        data = self.client.call(
            self.service,
            'getL7Policies',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Policy import L7Policy
        return SL_L7Policy(data)


