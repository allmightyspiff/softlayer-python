from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_Listener(Entity):
    """The SoftLayer_Network_LBaaS_Listener type presents a data structure for a load balancers listener, also
called frontend."""
    clientTimeout: int
    connectionLimit: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    protocol: str
    protocolPort: int
    provisioningStatus: str
    serverTimeout: int
    tlsCertificateId: int
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_Listener'

    def deleteLoadBalancerProtocols(self, loadBalancerUuid: str, listenerUuids: str) -> 'Network_LBaaS_LoadBalancer':
        """Delete load balancers front- and backend protocols"""
        data = self.client.call('SoftLayer_Network_LBaaS_Listener', 'deleteLoadBalancerProtocols', loadBalancerUuid, listenerUuids)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_Listener':
        """Retrieve a SoftLayer_Network_LBaaS_Listener record."""
        data = self.client.call('SoftLayer_Network_LBaaS_Listener', 'getObject', id=identifier)
        return data

    def updateLoadBalancerProtocols(self, loadBalancerUuid: str, protocolConfigurations: 'Network_LBaaS_LoadBalancerProtocolConfiguration') -> 'Network_LBaaS_LoadBalancer':
        """Update/create load balancers protocols"""
        data = self.client.call('SoftLayer_Network_LBaaS_Listener', 'updateLoadBalancerProtocols', loadBalancerUuid, protocolConfigurations)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getDefaultPool(self, identifier: int) -> 'Network_LBaaS_Pool':
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_Listener', 'getDefaultPool', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_Pool import Network_LBaaS_Pool
        return data

    def getL7Policies(self, identifier: int) -> list['Network_LBaaS_L7Policy']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_Listener', 'getL7Policies', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Policy import Network_LBaaS_L7Policy
        return data
