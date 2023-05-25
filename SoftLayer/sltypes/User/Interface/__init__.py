from SoftLayer.sltypes.Entity import Entity

class User_Interface(Entity):
    """A SoftLayer_User_Interface represents a generic user instance within the SoftLayer API. The SoftLayer API
uses SoftLayer_User_Interfaces in cases where a user object could be one of many types of users. Currently
the [[SoftLayer_User_Customer]] and [[SoftLayer_User_Employee]] classes are abstracted by this type."""
