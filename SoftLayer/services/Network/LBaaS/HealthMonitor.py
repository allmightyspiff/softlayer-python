# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LBaaS_HealthMonitor(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LBaaS_HealthMonitor'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LBaaS_HealthMonitor':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LBaaS.HealthMonitor import HealthMonitor
        return HealthMonitor(data)


    def updateLoadBalancerHealthMonitors(
        self,
        loadBalancerUuid: str,
        healthMonitorConfigurations: SoftLayer_Network_LBaaS_LoadBalancerHealthMonitorConfiguration,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_LBaaS_LoadBalancer':

        data = self.client.call(
            self.service,
            'updateLoadBalancerHealthMonitors',
            loadBalancerUuid,
            healthMonitorConfigurations,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.LBaaS.LoadBalancer import LoadBalancer
        return LoadBalancer(data)


