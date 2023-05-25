from SoftLayer.sltypes.Container.User.Customer.External.Binding import Container_User_Customer_External_Binding
from SoftLayer.sltypes.Container_User_Customer_External_Binding import Container_User_Customer_External_Binding

class Container_User_Customer_External_Binding_Totp(Container_User_Customer_External_Binding):
    """Container classed used to hold portal token"""
    securityCode: str
