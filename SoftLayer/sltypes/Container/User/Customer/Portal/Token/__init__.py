from SoftLayer.sltypes.User.Customer import User_Customer
from SoftLayer.sltypes.Entity import Entity

class Container_User_Customer_Portal_Token(Entity):
    """Container classed used to hold portal token"""
    hash_: str
    user: User_Customer
    userId: int
