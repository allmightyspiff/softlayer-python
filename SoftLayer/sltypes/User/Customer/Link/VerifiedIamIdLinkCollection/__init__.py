from SoftLayer.sltypes.User.Customer.Link import User_Customer_Link
from SoftLayer.sltypes.Entity import Entity

class User_Customer_Link_VerifiedIamIdLinkCollection(Entity):
    badLinksDifferentIUI: list[User_Customer_Link]
    badLinksDifferentUsername: list[User_Customer_Link]
    goodLinks: list[User_Customer_Link]
