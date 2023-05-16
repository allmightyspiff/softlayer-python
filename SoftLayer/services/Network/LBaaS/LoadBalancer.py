# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_LoadBalancer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_LoadBalancer'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def cancelLoadBalancer(
        self,
        uuid: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'cancelLoadBalancer',
            uuid
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def enableOrDisableDataLogs(
        self,
        uuid: str,
        enabled: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'enableOrDisableDataLogs',
            uuid,
            enabled,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_LoadBalancer]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getListenerTimeSeriesData(
        self,
        loadBalancerUuid: str,
        metricName: str,
        timeRange: str,
        listenerUuid: str
    ) -> 'list[SoftLayer_Network_LBaaS_LoadBalancerMonitoringMetricDataPoint]':
        data = self.client.call(
            self.service,
            'getListenerTimeSeriesData',
            loadBalancerUuid,
            metricName,
            timeRange,
            listenerUuid
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancerMonitoringMetricDataPoint import LoadBalancerMonitoringMetricDataPoint
        return SL_LoadBalancerMonitoringMetricDataPoint(data)

# This file was automatically generated with tools/generateTypes.py
    def getLoadBalancer(
        self,
        uuid: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'getLoadBalancer',
            uuid,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getLoadBalancerMemberHealth(
        self,
        uuid: str
    ) -> 'list[SoftLayer_Network_LBaaS_PoolMembersHealth]':
        data = self.client.call(
            self.service,
            'getLoadBalancerMemberHealth',
            uuid
        )
        from SoftLayer.datatypes.Network.LBaaS.PoolMembersHealth import PoolMembersHealth
        return SL_PoolMembersHealth(data)

# This file was automatically generated with tools/generateTypes.py
    def getLoadBalancerStatistics(
        self,
        uuid: str
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancerStatistics':
        data = self.client.call(
            self.service,
            'getLoadBalancerStatistics',
            uuid
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancerStatistics import LoadBalancerStatistics
        return SL_LoadBalancerStatistics(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def serviceLoadBalancer(
        self,
        data: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'serviceLoadBalancer',
            data,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def updateLoadBalancer(
        self,
        uuid: str,
        newDescription: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'updateLoadBalancer',
            uuid,
            newDescription,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def updateSslCiphers(
        self,
        loadBalancerUuid: str,
        cipherList: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':
        data = self.client.call(
            self.service,
            'updateSslCiphers',
            loadBalancerUuid,
            cipherList,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return SL_LoadBalancer(data)

# This file was automatically generated with tools/generateTypes.py
    def getDatacenter(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getDatacenter',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getHealthMonitors(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_HealthMonitor]':
        data = self.client.call(
            self.service,
            'getHealthMonitors',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.HealthMonitor import HealthMonitor
        return SL_HealthMonitor(data)

# This file was automatically generated with tools/generateTypes.py
    def getL7Pools(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_L7Pool]':
        data = self.client.call(
            self.service,
            'getL7Pools',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Pool import L7Pool
        return SL_L7Pool(data)

# This file was automatically generated with tools/generateTypes.py
    def getListeners(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_Listener]':
        data = self.client.call(
            self.service,
            'getListeners',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.Listener import Listener
        return SL_Listener(data)

# This file was automatically generated with tools/generateTypes.py
    def getMembers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_Member]':
        data = self.client.call(
            self.service,
            'getMembers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.Member import Member
        return SL_Member(data)

# This file was automatically generated with tools/generateTypes.py
    def getSslCiphers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_SSLCipher]':
        data = self.client.call(
            self.service,
            'getSslCiphers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.SSLCipher import SSLCipher
        return SL_SSLCipher(data)


