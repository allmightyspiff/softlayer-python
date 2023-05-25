from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LBaaS_L7Rule(Entity):
    """The SoftLayer_Network_LBaaS_L7Rule represents the Rules that can be attached to a a L7 policy."""
    comparisonType: str
    createDate: datetime
    id_: int
    invert: int
    key: str
    modifyDate: datetime
    type_: str
    uuid: str
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LBaaS_L7Rule'

    def addL7Rules(self, policyUuid: str, rules: 'Network_LBaaS_L7Rule') -> 'Network_LBaaS_LoadBalancer':
        """Create and add a L7 Rule to a given L7 policy with the provided rules details."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Rule', 'addL7Rules', policyUuid, rules)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def deleteL7Rules(self, policyUuid: str, ruleUuids: str) -> 'Network_LBaaS_LoadBalancer':
        """Delete one or more rules associated with the same policy."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Rule', 'deleteL7Rules', policyUuid, ruleUuids)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data

    def getObject(self, identifier: int) -> 'Network_LBaaS_L7Rule':
        """Retrieve a SoftLayer_Network_LBaaS_L7Rule record."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Rule', 'getObject', id=identifier)
        return data

    def updateL7Rules(self, policyUuid: str, rules: 'Network_LBaaS_L7Rule') -> 'Network_LBaaS_LoadBalancer':
        """Update one or more rules associated with the same policy."""
        data = self.client.call('SoftLayer_Network_LBaaS_L7Rule', 'updateL7Rules', policyUuid, rules)
        from SoftLayer.sltypes.Network_LBaaS_LoadBalancer import Network_LBaaS_LoadBalancer
        return data
