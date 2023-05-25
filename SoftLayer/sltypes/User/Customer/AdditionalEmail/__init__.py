from SoftLayer.sltypes.Entity import Entity

class User_Customer_AdditionalEmail(Entity):
    """The SoftLayer_User_Customer_AdditionalEmail data type contains the additional email for use in ticket update
notifications."""
    email: str
    userId: int
