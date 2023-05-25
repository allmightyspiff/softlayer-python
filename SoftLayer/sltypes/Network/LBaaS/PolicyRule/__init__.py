from SoftLayer.sltypes.Network.LBaaS.L7Rule import Network_LBaaS_L7Rule
from SoftLayer.sltypes.Network.LBaaS.L7Policy import Network_LBaaS_L7Policy
from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_PolicyRule(Entity):
    """SoftLayer_Network_LBaaS_PolicyRule   This class contains layer 7 policy specifications and an array of
associated rules An array of objects of this class must be passed to the API in order to create a policy and
its associated rules. <ul> <li>The layer 7 policy object </li> <li>An array of layer 7 rules </li> </ul>"""
    l7Policy: Network_LBaaS_L7Policy
    l7Rules: list[Network_LBaaS_L7Rule]
