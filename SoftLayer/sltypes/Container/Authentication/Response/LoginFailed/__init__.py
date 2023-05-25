from SoftLayer.sltypes.Container.Authentication.Response.Common import Container_Authentication_Response_Common
from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common

class Container_Authentication_Response_LoginFailed(Container_Authentication_Response_Common):
    """The SoftLayer_Container_Authentication_Response_LOGIN_FAILED data type contains information for specific
responses from the getPortalLogin API. This class is indicative of a request where there was an inability to
login based on the information that was provided."""
    errorMessage: str
    statusKeyName: str
