from SoftLayer.sltypes.Container.Utility.Network.Subnet.Mask.Generic.Detail import Container_Utility_Network_Subnet_Mask_Generic_Detail
from SoftLayer.sltypes.Entity import Entity

class Container_Utility_Network_Firewall_Rule_Attribute(Entity):
    """The SoftLayer_Container_Utility_Network_Firewall_Rule_Attribute data type contains information relating to a
single firewall rule."""
    actions: list[str]
    maximumRuleCount: int
    protocols: list[str]
    sourceIpSubnetMasks: list[Container_Utility_Network_Subnet_Mask_Generic_Detail]
