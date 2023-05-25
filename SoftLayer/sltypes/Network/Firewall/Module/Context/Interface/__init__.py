from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Firewall_Module_Context_Interface(Entity):
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_Module_Context_Interface'

    def getObject(self, identifier: int) -> 'Network_Firewall_Module_Context_Interface':
        """Retrieve a SoftLayer_Network_Firewall_Module_Context_Interface record."""
        data = self.client.call('SoftLayer_Network_Firewall_Module_Context_Interface', 'getObject', id=identifier)
        return data

    def getFirewallContextAccessControlLists(self, identifier: int) -> list['Network_Firewall_AccessControlList']:
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Module_Context_Interface', 'getFirewallContextAccessControlLists', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_AccessControlList import Network_Firewall_AccessControlList
        return data

    def getNetworkVlan(self, identifier: int) -> 'Network_Vlan':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Module_Context_Interface', 'getNetworkVlan', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data
