# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_LoadBalancer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_LoadBalancer'
        self.client = client

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


    def enableOrDisableDataLogs(
        self,
        uuid: str,
        enabled: bool,
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
        return LoadBalancer(data)


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
        return LoadBalancer(data)


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
        return LoadBalancerMonitoringMetricDataPoint(data)


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
        return LoadBalancer(data)


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
        return PoolMembersHealth(data)


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
        return LoadBalancerStatistics(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


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
        return LoadBalancer(data)


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
        return LoadBalancer(data)


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
        return LoadBalancer(data)


    def getDatacenter(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getDatacenter',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getHealthMonitors(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_HealthMonitor]':

        data = self.client.call(
            self.service,
            'getHealthMonitors',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.HealthMonitor import HealthMonitor
        return HealthMonitor(data)


    def getL7Pools(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_L7Pool]':

        data = self.client.call(
            self.service,
            'getL7Pools',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.L7Pool import L7Pool
        return L7Pool(data)


    def getListeners(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_Listener]':

        data = self.client.call(
            self.service,
            'getListeners',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.Listener import Listener
        return Listener(data)


    def getMembers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_Member]':

        data = self.client.call(
            self.service,
            'getMembers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.Member import Member
        return Member(data)


    def getSslCiphers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_SSLCipher]':

        data = self.client.call(
            self.service,
            'getSslCiphers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.SSLCipher import SSLCipher
        return SSLCipher(data)


