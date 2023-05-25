from SoftLayer.sltypes.Container.Authentication.Response.Common import Container_Authentication_Response_Common
from SoftLayer.sltypes.Container_Authentication_Response_Common import Container_Authentication_Response_Common

class Container_Authentication_Response_IpAddressRestrictionCheckNeeded(Container_Authentication_Response_Common):
    """The SoftLayer_Container_Authentication_Response_IpAddressRestrictionCheckNeeded data type indicates that the
caller (IAM presumably) needs to do an IP address check of the logging-in user against the restricted IP list
kept in BSS.  We don't know the IP address of the user here (only IAM does) so we return an indicator of
which user matched the username and expect IAM to come back with another login call that will include a mini-
JWT token that contains an assertion that the IP address was checked."""
    statusKeyName: str
