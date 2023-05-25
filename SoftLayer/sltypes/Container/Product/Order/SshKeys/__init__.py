from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order_SshKeys(Entity):
    """This object holds all of the ssh key ids that will allow authentication to a single server."""
    sshKeyIds: list[int]
