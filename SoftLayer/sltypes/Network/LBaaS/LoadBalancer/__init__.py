from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_LoadBalancer(Entity):
    """The SoftLayer_Network_LBaaS_LoadBalancer type presents a structure containing attributes of a load balancer,
and its related objects including listeners, pools and members."""
    accountId: int
    address: str
    createDate: datetime
    description: str
    id_: int
    isDataLogEnabled: int
    isPublic: int
    locationId: int
    modifyDate: datetime
    name: str
    operatingStatus: str
    previousErrorText: str
    provisioningStatus: str
    type_: int
    useSystemPublicIpPool: int
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_LoadBalancer'

    def cancelLoadBalancer(self, uuid: str) -> bool:
        """Cancel the specified load balancer."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'cancelLoadBalancer', uuid)
        return data

    def enableOrDisableDataLogs(self, uuid: str, enabled: bool) -> 'Network_LBaaS_LoadBalancer':
        """Enable or disable data logs forwarding."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'enableOrDisableDataLogs', uuid, enabled)
        return data

    def getAllObjects(self) -> list['Network_LBaaS_LoadBalancer']:
        """Get all existing load balancers."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getAllObjects')
        return data

    def getListenerTimeSeriesData(self, loadBalancerUuid: str, metricName: str, timeRange: str, listenerUuid: str) -> list['Network_LBaaS_LoadBalancerMonitoringMetricDataPoint']:
        """Return time series datapoints"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getListenerTimeSeriesData', loadBalancerUuid, metricName, timeRange, listenerUuid)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancerMonitoringMetricDataPoint import Network_LBaaS_LoadBalancerMonitoringMetricDataPoint
        return data

    def getLoadBalancer(self, uuid: str) -> 'Network_LBaaS_LoadBalancer':
        """Get a specific load balancer."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getLoadBalancer', uuid)
        return data

    def getLoadBalancerMemberHealth(self, uuid: str) -> list['Network_LBaaS_PoolMembersHealth']:
        """Return load balancer members health"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getLoadBalancerMemberHealth', uuid)
        from SoftLayer.sltypes.Network_LBaaS_PoolMembersHealth import Network_LBaaS_PoolMembersHealth
        return data

    def getLoadBalancerStatistics(self, uuid: str) -> 'Network_LBaaS_LoadBalancerStatistics':
        """Return load balancers statistics"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getLoadBalancerStatistics', uuid)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancerStatistics import Network_LBaaS_LoadBalancerStatistics
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_LoadBalancer':
        """Retrieve a SoftLayer_Network_LBaaS_LoadBalancer record."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getObject', id=identifier)
        return data

    def serviceLoadBalancer(self, data: str) -> 'Network_LBaaS_LoadBalancer':
        """Service function for a load balancer."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'serviceLoadBalancer', data)
        return data

    def updateLoadBalancer(self, uuid: str, newDescription: str) -> 'Network_LBaaS_LoadBalancer':
        """Update a load balancer's description."""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'updateLoadBalancer', uuid, newDescription)
        return data

    def updateSslCiphers(self, loadBalancerUuid: str, cipherList: int) -> 'Network_LBaaS_LoadBalancer':
        """Updates the cipher list of the load balancer"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'updateSslCiphers', loadBalancerUuid, cipherList)
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getHealthMonitors(self, identifier: int) -> list['Network_LBaaS_HealthMonitor']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getHealthMonitors', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_HealthMonitor import Network_LBaaS_HealthMonitor
        return data

    def getL7Pools(self, identifier: int) -> list['Network_LBaaS_L7Pool']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getL7Pools', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Pool import Network_LBaaS_L7Pool
        return data

    def getListeners(self, identifier: int) -> list['Network_LBaaS_Listener']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getListeners', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_Listener import Network_LBaaS_Listener
        return data

    def getMembers(self, identifier: int) -> list['Network_LBaaS_Member']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getMembers', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_Member import Network_LBaaS_Member
        return data

    def getSslCiphers(self, identifier: int) -> list['Network_LBaaS_SSLCipher']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_LoadBalancer', 'getSslCiphers', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_SSLCipher import Network_LBaaS_SSLCipher
        return data
