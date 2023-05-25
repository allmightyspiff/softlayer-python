from SoftLayer.sltypes.Entity import Entity

class Network_Firewall_Template_Rule(Entity):
    """The SoftLayer_Network_Component_Firewall_Rule type contains general information relating to a single
SoftLayer firewall template rule. Use the [[SoftLayer Network Component Firewall]] service to view current
rules. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request."""
    action: str
    destinationIpAddress: str
    destinationIpSubnetMask: str
    destinationPortRangeEnd: int
    destinationPortRangeStart: int
    firewallTemplateId: int
    id_: int
    notes: str
    orderValue: int
    protocol: str
    sourceIpAddress: str
    sourceIpSubnetMask: str
