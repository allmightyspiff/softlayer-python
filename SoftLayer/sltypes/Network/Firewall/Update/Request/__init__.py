from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Firewall_Update_Request(Entity):
    """The SoftLayer_Network_Firewall_Update_Request data type contains information relating to a SoftLayer network
firewall update request. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use
the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule set templates."""
    applyDate: datetime
    authorizingUserId: int
    authorizingUserType: str
    bypassFlag: bool
    createDate: datetime
    firewallContextAccessControlListId: int
    hardwareId: int
    id_: int
    networkComponentFirewallId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_Update_Request'

    def createObject(self, templateObject: 'Network_Firewall_Update_Request') -> 'Network_Firewall_Update_Request':
        """Create a new firewall update request."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data

    def getFirewallUpdateRequestRuleAttributes(self) -> 'Container_Utility_Network_Firewall_Rule_Attribute':
        """Get the possible attribute values for a firewall update request rule."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getFirewallUpdateRequestRuleAttributes')
        from SoftLayer.sltypes.Container_Utility_Network_Firewall_Rule_Attribute import Container_Utility_Network_Firewall_Rule_Attribute
        return data

    def getObject(self, identifier: int) -> 'Network_Firewall_Update_Request':
        """Retrieve a SoftLayer_Network_Firewall_Update_Request record."""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request import Network_Firewall_Update_Request
        return data

    def updateRuleNote(self, fwRule: 'Network_Component_Firewall_Rule', note: str) -> bool:
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'updateRuleNote', fwRule, note)
        return data

    def getAuthorizingUser(self, identifier: int) -> 'User_Interface':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getAuthorizingUser', id=identifier)
        from SoftLayer.sltypes.User_Interface import User_Interface
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkComponentFirewall(self, identifier: int) -> 'Network_Component_Firewall':
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getNetworkComponentFirewall', id=identifier)
        from SoftLayer.sltypes.Network_Component_Firewall import Network_Component_Firewall
        return data

    def getRules(self, identifier: int) -> list['Network_Firewall_Update_Request_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Update_Request', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Update_Request_Rule import Network_Firewall_Update_Request_Rule
        return data
