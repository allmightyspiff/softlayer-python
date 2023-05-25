from SoftLayer.sltypes.Container.Authentication.Request.Common import Container_Authentication_Request_Common
from SoftLayer.sltypes.Container_Authentication_Request_Common import Container_Authentication_Request_Common

class Container_Authentication_Request_Native(Container_Authentication_Request_Common):
    """The SoftLayer_Container_Authentication_Request_Native data type contains information for requests to the
getPortalLogin API. This class is specific to the SoftLayer Native login (username/password). The request
information will be verified to ensure it is valid, and then there will be an attempt to obtain a portal
login token in authenticating the user with the provided information."""
    auxiliaryClaimsMiniToken: str
    password: str
    username: str
