from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Component_Firewall(Entity):
    """The SoftLayer_Network_Component_Firewall data type contains general information relating to a single
SoftLayer network component firewall. This is the object which ties the running rules to a specific
downstream server. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule
set templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update
request."""
    guestNetworkComponentId: int
    id_: int
    networkComponentId: int
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Component_Firewall'

    def getObject(self, identifier: int) -> 'Network_Component_Firewall':
        """Retrieve a SoftLayer_Network_Component_Firewall record."""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getObject', id=identifier)
        return data

    def hasActiveTransactions(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'hasActiveTransactions', id=identifier)
        return data

    def getApplyServerRuleSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getApplyServerRuleSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getGuestNetworkComponent(self, identifier: int) -> 'Virtual_Guest_Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getGuestNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Network_Component import Virtual_Guest_Network_Component
        return data

    def getNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data

    def getNetworkFirewallUpdateRequest(self, identifier: int) -> list['Network_Firewall_Update_Request']:
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getNetworkFirewallUpdateRequest', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data

    def getRules(self, identifier: int) -> list['Network_Component_Firewall_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall_Rule import Network_Component_Firewall_Rule
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Component_Firewall', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
