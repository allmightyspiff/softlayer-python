from SoftLayer.sltypes.Entity import Entity

class Network_Component_Network_Vlan_Trunk(Entity):
    """Represents the association between a Network_Component and Network_Vlan in the manner of a 'trunk'. Trunking
a VLAN to a port allows that ports to receive and send packets tagged with the corresponding VLAN number."""
    networkComponentId: int
    networkVlanId: int
