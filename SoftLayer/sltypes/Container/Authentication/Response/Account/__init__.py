from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Authentication_Response_Account(Entity):
    """The SoftLayer_Container_Authentication_Response_Account data type contains account information for responses
from the getPortalLogin API."""
    accountCompanyName: str
    accountCountry: str
    accountId: int
    accountStatusName: str
    bluemixAccountId: str
    createDate: datetime
    defaultAccount: bool
    ipAddressCheckRequired: bool
    isMasterUserFlag: bool
    modifyDate: datetime
    securityQuestionRequired: bool
    totpExternalAuthenticationRequired: bool
    userId: int
    verisignExternalAuthenticationRequired: bool
