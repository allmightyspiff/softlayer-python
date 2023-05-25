from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Firewall_Update_Request_Rule(Entity):
    """The SoftLayer_Network_Firewall_Update_Request_Rule type contains information relating to a SoftLayer network
firewall update request rule. This rule is a member of a [[SoftLayer Network Firewall Update Request]]. Use
the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network
Firewall Template]] service to pull SoftLayer recommended rule set templates."""
    action: str
    bypassRuleValidation: bool
    destinationIpAddress: str
    destinationIpCidr: int
    destinationIpSubnetMask: str
    destinationPortRangeEnd: int
    destinationPortRangeStart: int
    firewallUpdateRequestId: int
    id_: int
    notes: str
    orderValue: int
    protocol: str
    sourceIpAddress: str
    sourceIpCidr: int
    sourceIpSubnetMask: str
    version: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_Update_Request_Rule'

    def createObject(self, templateObject: 'Network_Firewall_Update_Request_Rule') -> 'Network_Firewall_Update_Request_Rule':
        """Create a new firewall update request rule."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request_Rule', 'createObject', templateObject)
        return data

    def getObject(self, identifier: int) -> 'Network_Firewall_Update_Request_Rule':
        """Retrieve a SoftLayer_Network_Firewall_Update_Request_Rule record."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request_Rule', 'getObject', id=identifier)
        return data

    def validateRule(self, rule: 'Network_Firewall_Update_Request_Rule', applyToComponentId: int, applyToAclId: int) -> None:
        """Validate a firewall update request rule."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request_Rule', 'validateRule', rule, applyToComponentId, applyToAclId)
        return data

    def getFirewallUpdateRequest(self, identifier: int) -> 'Network_Firewall_Update_Request':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request_Rule', 'getFirewallUpdateRequest', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data
