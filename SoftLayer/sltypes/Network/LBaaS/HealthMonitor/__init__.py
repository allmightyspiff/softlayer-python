from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_HealthMonitor(Entity):
    """The SoftLayer_Network_LBaaS_HealthMonitor type presents a structure containing attributes of a health monitor
object associated with load balancer instance. Note that the relationship between backend (pool) and health
monitor is N-to-1, especially that the pools object associated with a health monitor must have the same pair
of protocol and port. Example: frontend FA: http, 80   - backend BA: tcp, 3456 - healthmonitor HM_tcp3456
frontend FB: https, 443 - backend BB: tcp, 3456 - healthmonitor HM_tcp3456 In above example both backends BA
and BB share the same healthmonitor HM_tcp3456"""
    createDate: datetime
    id_: int
    interval: int
    maxRetries: int
    modifyDate: datetime
    monitorType: str
    provisioningStatus: str
    timeout: int
    urlPath: str
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_HealthMonitor'

    def getObject(self, identifier: int) -> 'Network_LBaaS_HealthMonitor':
        """Retrieve a SoftLayer_Network_LBaaS_HealthMonitor record."""
        data = self.client.call('SoftLayer_Network_LBaaS_HealthMonitor', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_HealthMonitor import Network_LBaaS_HealthMonitor
        return data

    def updateLoadBalancerHealthMonitors(self, loadBalancerUuid: str, healthMonitorConfigurations: 'Network_LBaaS_LoadBalancerHealthMonitorConfiguration') -> 'Network_LBaaS_LoadBalancer':
        """Update load balancer health monitors"""
        data = self.client.call('SoftLayer_Network_LBaaS_HealthMonitor', 'updateLoadBalancerHealthMonitors', loadBalancerUuid, healthMonitorConfigurations)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data
