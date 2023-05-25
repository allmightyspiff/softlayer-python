from SoftLayer.sltypes.Entity import Entity

class Network_Component_Firewall_Subnets(Entity):
    """A SoftLayer_Network_Component_Firewall_Subnets object type represents the current linked subnets and contains
relative information. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall
update request. Use the [[SoftLayer Network Firewall Template]] service to pull SoftLayer recommended rule
set templates."""
    applyServerRulesFlag: bool
    subnetId: int
