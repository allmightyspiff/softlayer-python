# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_L7Pool(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_L7Pool'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createL7Pool(
        self,
        loadBalancerUuid: str,
        l7Pool: SoftLayer_Network_LBaaS_L7Pool,
        l7Members: SoftLayer_Network_LBaaS_L7Member,
        l7HealthMonitor: SoftLayer_Network_LBaaS_L7HealthMonitor,
        l7SessionAffinity: SoftLayer_Network_LBaaS_L7SessionAffinity,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'createL7Pool',
            loadBalancerUuid,
            l7Pool,
            l7Members,
            l7HealthMonitor,
            l7SessionAffinity,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'deleteObject',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getL7PoolMemberHealth(
        self,
        loadBalancerUuid: str
    ) -> 'list[SoftLayer_Network_LBaaS_L7PoolMembersHealth]':
        data = self.client.call(
            self.service,
            'getL7PoolMemberHealth',
            loadBalancerUuid
        )
        from SoftLayer.datatypes.Network.LBaaS.L7PoolMembersHealth import L7PoolMembersHealth
        return SL_L7PoolMembersHealth(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_L7Pool':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Pool import L7Pool
        return SL_L7Pool(data)

# This file was automatically generated with tools/generateTypes.py
    def updateL7Pool(
        self,
        l7PoolUuid: str,
        l7Pool: SoftLayer_Network_LBaaS_L7Pool,
        l7HealthMonitor: SoftLayer_Network_LBaaS_L7HealthMonitor,
        l7SessionAffinity: SoftLayer_Network_LBaaS_L7SessionAffinity,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'updateL7Pool',
            l7PoolUuid,
            l7Pool,
            l7HealthMonitor,
            l7SessionAffinity,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getL7HealthMonitor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_L7HealthMonitor':
        data = self.client.call(
            self.service,
            'getL7HealthMonitor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.L7HealthMonitor import L7HealthMonitor
        return SL_L7HealthMonitor(data)

# This file was automatically generated with tools/generateTypes.py
    def getL7Members(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_L7Member]':
        data = self.client.call(
            self.service,
            'getL7Members',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Member import L7Member
        return SL_L7Member(data)

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

# This file was automatically generated with tools/generateTypes.py
    def getL7SessionAffinity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_L7SessionAffinity':
        data = self.client.call(
            self.service,
            'getL7SessionAffinity',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.L7SessionAffinity import L7SessionAffinity
        return SL_L7SessionAffinity(data)


