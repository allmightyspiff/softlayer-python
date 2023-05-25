from SoftLayer.sltypes.Entity import Entity

class Network_SecurityGroup_Request(Entity):
    """The SoftLayer_Network_SecurityGroup_Request data type contains the ID of a specific request sent to the API.
This ID is used to identify specific calls to attach and detach network components, as well as add, edit, and
remove security group rules."""
    requestId: str
