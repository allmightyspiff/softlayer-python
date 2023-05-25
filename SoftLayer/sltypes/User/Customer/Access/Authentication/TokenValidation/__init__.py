from SoftLayer.sltypes.User.Customer.Access.Authentication import User_Customer_Access_Authentication
from SoftLayer.sltypes.User_Customer_Access_Authentication import User_Customer_Access_Authentication

class User_Customer_Access_Authentication_TokenValidation(User_Customer_Access_Authentication):
    """SoftLayer_User_Customer_Access_Authentication_TokenValidation is for logging token validations from IAM, as
something distinct from a traditional "login".  A single login to IBM Cloud/IAM as perceived by the end user,
may result in many token validation calls to IMS.   This is a very shallow subclass of
SoftLayer_User_Customer_Access_Authentication"""
