from SoftLayer.sltypes.Entity import Entity

class Account_Attachment_Employee(Entity):
    """A SoftLayer_Account_Attachment_Employee models an assignment of a single [[SoftLayer_User_Employee|employee]]
with a single [[SoftLayer_Account|account]]"""
    roleId: int
