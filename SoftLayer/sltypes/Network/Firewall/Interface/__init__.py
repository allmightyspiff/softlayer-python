from SoftLayer.sltypes.Network.Firewall.Module.Context.Interface import Network_Firewall_Module_Context_Interface
from SoftLayer.sltypes.Network_Firewall_Module_Context_Interface import Network_Firewall_Module_Context_Interface
from SoftLayer import BaseClient

class Network_Firewall_Interface(Network_Firewall_Module_Context_Interface):
    """The SoftLayer_Network_Firewall_Interface data type contains general information relating to a single
SoftLayer firewall interface. This is the object which ties the firewall context access control list to a
firewall. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set
templates. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_Interface'

    def getObject(self, identifier: int) -> 'Network_Firewall_Interface':
        """Retrieve a SoftLayer_Network_Firewall_Interface record."""
        data = self.client.call('SoftLayer_Network_Firewall_Interface', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Interface import Network_Firewall_Interface
        return data
