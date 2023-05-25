from SoftLayer.sltypes.Software.Component import Software_Component
from SoftLayer.sltypes.Software_Component import Software_Component
from SoftLayer import BaseClient

class Software_Component_HostIps(Software_Component):
    """This object specifies a specific type of Software Component:  A Host Intrusion Protection System instance."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_Component_HostIps'

    def getCurrentHostIpsPolicies(self, identifier: int) -> list['Container_Software_Component_HostIps_Policy']:
        """Get the current Host IPS policies."""
        data = self.client.call('SoftLayer_Software_Component_HostIps', 'getCurrentHostIpsPolicies', id=identifier)
        from SoftLayer.sltypes.Container_Software_Component_HostIps_Policy import Container_Software_Component_HostIps_Policy
        return data

    def getObject(self, identifier: int) -> 'Software_Component_HostIps':
        """Retrieve a SoftLayer_Software_Component_HostIps record."""
        data = self.client.call('SoftLayer_Software_Component_HostIps', 'getObject', id=identifier)
        return data

    def updateHipsPolicies(self, identifier: int, newIpsMode: str, newIpsProtection: str, newFirewallMode: str, newFirewallRuleset: str, newApplicationMode: str, newApplicationRuleset: str, newEnforcementPolicy: str) -> bool:
        """Update the Host IPS policies."""
        data = self.client.call('SoftLayer_Software_Component_HostIps', 'updateHipsPolicies', newIpsMode, newIpsProtection, newFirewallMode, newFirewallRuleset, newApplicationMode, newApplicationRuleset, newEnforcementPolicy, id=identifier)
        return data
