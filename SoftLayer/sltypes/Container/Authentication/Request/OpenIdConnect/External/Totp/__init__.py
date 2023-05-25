from SoftLayer.sltypes.Container.Authentication.Request.OpenIdConnect.External import Container_Authentication_Request_OpenIdConnect_External
from SoftLayer.sltypes.Container_Authentication_Request_OpenIdConnect_External import Container_Authentication_Request_OpenIdConnect_External

class Container_Authentication_Request_OpenIdConnect_External_Totp(Container_Authentication_Request_OpenIdConnect_External):
    """The SoftLayer_Container_Authentication_Request_OpenIdConnect_External_Totp data type contains information for
requests to the getPortalLogin API. This class provides information to allow the user to submit a request to
the SoftLayer OpenIdConnect (token) login service for a portal login token, as well as submitting a request
to the TOTP 2 factor authentication service."""
    secondSecurityCode: str
    securityCode: str
    vendor: str
