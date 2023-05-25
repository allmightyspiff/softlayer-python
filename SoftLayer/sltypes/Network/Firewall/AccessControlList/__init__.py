from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Firewall_AccessControlList(Entity):
    """The SoftLayer_Network_Firewall_AccessControlList data type contains general information relating to a single
SoftLayer firewall access to controll list. This is the object which ties the running rules to a specific
context. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set
templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request."""
    direction: str
    firewallContextInterfaceId: int
    id_: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_AccessControlList'

    def getObject(self, identifier: int) -> 'Network_Firewall_AccessControlList':
        """Retrieve a SoftLayer_Network_Firewall_AccessControlList record."""
        data = self.client.call('SoftLayer_Network_Firewall_AccessControlList', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_AccessControlList import Network_Firewall_AccessControlList
        return data

    def getNetworkFirewallUpdateRequests(self, identifier: int) -> list['Network_Firewall_Update_Request']:
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_AccessControlList', 'getNetworkFirewallUpdateRequests', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_AccessControlList', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getRules(self, identifier: int) -> list['Network_Vlan_Firewall_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_AccessControlList', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_Vlan_Firewall_Rule import Network_Vlan_Firewall_Rule
        return data
