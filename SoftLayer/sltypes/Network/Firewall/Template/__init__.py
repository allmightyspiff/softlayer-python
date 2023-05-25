from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Firewall_Template(Entity):
    """The SoftLayer_Network_Firewall_Template type contains general information for a SoftLayer network firewall
template.   Firewall templates are recommend rule sets for use with SoftLayer Hardware Firewall (Dedicated).
These optimized templates are designed to balance security restriction with application availability.  The
templates given may be altered to provide custom network security, or may be used as-is for basic security.
At least one rule set MUST be applied for the firewall to block traffic. Use the [[SoftLayer Network
Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Update Request]]
service to submit a firewall update request."""
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Firewall_Template'

    def getAllObjects(self) -> list['Network_Firewall_Template']:
        """Get all available firewall template objects."""
        data = self.client.call('SoftLayer_Network_Firewall_Template', 'getAllObjects')
        from SoftLayer.sltypes.Network_Firewall_Template import Network_Firewall_Template
        return data

    def getObject(self, identifier: int) -> 'Network_Firewall_Template':
        """Retrieve a SoftLayer_Network_Firewall_Template record."""
        data = self.client.call('SoftLayer_Network_Firewall_Template', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Template import Network_Firewall_Template
        return data

    def getRules(self, identifier: int) -> list['Network_Firewall_Template_Rule']:
        """"""
        data = self.client.call('SoftLayer_Network_Firewall_Template', 'getRules', id=identifier)
        from SoftLayer.sltypes.Network_Firewall_Template_Rule import Network_Firewall_Template_Rule
        return data
