from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_L7Policy(Entity):
    """The SoftLayer_Network_LBaaS_L7Policy represents the policy for a listener."""
    action: str
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    priority: int
    redirectL7PoolId: int
    redirectL7PoolUuid: str
    redirectUrl: str
    uuid: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_L7Policy'

    def addL7Policies(self, listenerUuid: str, policiesRules: 'Network_LBaaS_PolicyRule') -> 'Network_LBaaS_LoadBalancer':
        """Create layer 7 policies with rules for the given listener."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Policy', 'addL7Policies', listenerUuid, policiesRules)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def deleteObject(self, identifier: int) -> 'Network_LBaaS_LoadBalancer':
        """Deletes a l7 policy instance and the rules associated with the policy"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Policy', 'deleteObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def editObject(self, identifier: int, templateObject: 'Network_LBaaS_L7Policy') -> 'Network_LBaaS_LoadBalancer':
        """Edit a l7 policy instance's properties"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Policy', 'editObject', templateObject, id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_L7Policy':
        """Retrieve a SoftLayer_Network_LBaaS_L7Policy record."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Policy', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Policy import Network_LBaaS_L7Policy
        return data

    def getL7Rules(self, identifier: int) -> list['Network_LBaaS_L7Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Policy', 'getL7Rules', id=identifier)
        from SoftLayer.sltypes.Network_LBaaS_L7Rule import Network_LBaaS_L7Rule
        return data
