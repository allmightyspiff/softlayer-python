from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Block_Device_Template_Group_Status(Entity):
    """The virtual block device template group status data type represents the current status of the image template.
Depending upon the status, the image template can be used for provisioning or reloading.   For an operating
system reload, the image template will need to have a status of 'Active' or 'Deprecated'. For a provision,
the image template will need to have a status of 'Active'"""
    description: str
    keyName: str
    name: str
