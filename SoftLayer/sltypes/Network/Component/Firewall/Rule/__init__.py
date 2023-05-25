from SoftLayer.sltypes.Entity import Entity

class Network_Component_Firewall_Rule(Entity):
    """A SoftLayer_Network_Component_Firewall_Rule object type represents a currently running firewall rule and
contains relative information. Use the [[SoftLayer Network Firewall Update Request]] service to submit a
firewall update request. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer
recommended rule set templates."""
    action: str
    destinationIpAddress: str
    destinationIpCidr: int
    destinationIpSubnetMask: str
    destinationPortRangeEnd: int
    destinationPortRangeStart: int
    id_: int
    notes: str
    orderValue: int
    protocol: str
    sourceIpAddress: str
    sourceIpCidr: int
    sourceIpSubnetMask: str
    status: str
    version: int
