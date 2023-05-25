from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Block_Device_Template_Group_Accounts(Entity):
    """The SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts data type represents the SoftLayer customer
accounts which have access to provision CloudLayer Computing Instances from an image template group.   All
accounts other than the image template group owner have read-only access to that image template group.   It
is important to note that this data type should only exist to give accounts access to the parent template
group object, not the child.  All image template sharing between accounts should occur on the parent object."""
    accountId: int
    createDate: datetime
    groupId: int
