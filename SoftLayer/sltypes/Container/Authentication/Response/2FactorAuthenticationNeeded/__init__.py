from SoftLayer.sltypes.Container.Authentication.Response.Common import Container_Authentication_Response_Common
from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common

class Container_Authentication_Response_2FactorAuthenticationNeeded(Container_Authentication_Response_Common):
    """The SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded data type contains information
for specific responses from the getPortalLogin API. This class is indicative of a request that is missing the
appropriate 2FA information."""
    additionalData: Container_Authentication_Response_Common
    statusKeyName: str
