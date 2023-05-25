from SoftLayer.sltypes.Container.User.Authentication.Token import Container_User_Authentication_Token
from SoftLayer.sltypes.Container.Authentication.Response.Common import Container_Authentication_Response_Common
from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common

class Container_Authentication_Response_Success(Container_Authentication_Response_Common):
    """The SoftLayer_Container_Authentication_Response_SUCCESS data type contains information for specific responses
from the getPortalLogin API. This class is indicative of a request that was successful in obtaining a portal
login token from the getPortalLogin API."""
    statusKeyName: str
    token: Container_User_Authentication_Token
