from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth(Entity):
    """The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth data type contains
information for specific responses from the Token Authentication API."""
    aclDelimiter: str
    escapeTokenInputs: str
    hmacAlgorithm: str
    ignoreQueryString: str
    name: str
    path: str
    tokenDelimiter: str
    tokenKey: str
    transitionKey: str
    uniqueId: str
