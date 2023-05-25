from SoftLayer.sltypes.User.Customer import User_Customer
from SoftLayer.sltypes.Entity import Entity

class Container_User_Authentication_Token(Entity):
    """Container class used to hold user authentication token"""
    hash_: str
    user: User_Customer
    userId: int
