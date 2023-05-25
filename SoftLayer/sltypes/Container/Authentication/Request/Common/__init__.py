from SoftLayer.sltypes.Container.Authentication.Request.Contract import Container_Authentication_Request_Contract
from SoftLayer.sltypes.Container_Authentication_Request_Contract import Container_Authentication_Request_Contract

class Container_Authentication_Request_Common(Container_Authentication_Request_Contract):
    """The SoftLayer_Container_Authentication_Request_Common data type contains common information for requests to
the getPortalLogin API. This is an abstract class that serves as a base that more specialized classes will
derive from. For example, a request class specific to SoftLayer Native IMS Login (username and password)."""
    securityQuestionAnswer: str
    securityQuestionId: int
