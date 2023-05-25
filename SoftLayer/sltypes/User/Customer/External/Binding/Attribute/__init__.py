from SoftLayer.sltypes.User.External.Binding.Attribute import User_External_Binding_Attribute
from SoftLayer.sltypes.User_External_Binding_Attribute import User_External_Binding_Attribute

class User_Customer_External_Binding_Attribute(User_External_Binding_Attribute):
    """The SoftLayer_User_Customer_External_Binding_Attribute data type contains the value for a single attribute
associated with an external binding. External binding attributes contain additional information about an
external binding.  An attribute can be generic or specific to a 3rd party vendor.  For example these
attributes relate to Verisign:  *Credential Type *Credential State *Credential Expiration Date *Credential
Last Update Date"""
