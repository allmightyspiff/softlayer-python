from SoftLayer.sltypes.Entity import Entity

class Account_Password_Type(Entity):
    """Every username and password combination associated with a SoftLayer customer account belongs to a service
that SoftLayer provides. The relationship between a username/password and it's service is provided by the
SoftLayer_Account_Password_Type data type. Each username/password belongs to a single service type."""
    description: str
