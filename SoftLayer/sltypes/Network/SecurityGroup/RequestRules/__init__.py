from SoftLayer.sltypes.Network.SecurityGroup.Rule import Network_SecurityGroup_Rule
from SoftLayer.sltypes.Network.SecurityGroup.Request import Network_SecurityGroup_Request
from SoftLayer.sltypes.Network_SecurityGroup_Request import Network_SecurityGroup_Request

class Network_SecurityGroup_RequestRules(Network_SecurityGroup_Request):
    """The SoftLayer_Network_SecurityGroup_RequestRules data type contains the ID of a specific request sent to the
API, as well as an associative array of the rules that were created, edited, or removed by the request."""
    rules: list[Network_SecurityGroup_Rule]
