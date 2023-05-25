from SoftLayer.sltypes.Container.Authentication.Response.Account import Container_Authentication_Response_Account
from SoftLayer.sltypes.Entity import Entity

class Container_Authentication_Response_Common(Entity):
    """The SoftLayer_Container_Authentication_Response_Common data type contains common information for responses
from the getPortalLogin API. This is an abstract class that serves as a base that more specialized classes
will derive from. For example, a response class that is specific to a successful response from the
getPortalLogin API."""
    accounts: list[Container_Authentication_Response_Account]
