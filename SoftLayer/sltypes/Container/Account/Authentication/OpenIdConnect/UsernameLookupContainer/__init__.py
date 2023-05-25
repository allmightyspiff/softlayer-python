from SoftLayer.sltypes.Entity import Entity

class Container_Account_Authentication_OpenIdConnect_UsernameLookupContainer(Entity):
    active: bool
    emailAddress: str
    federated: bool
    foundAs: str
    numberOfIbmIdsWithEmailAddress: int
    realm: str
    uniqueId: str
    username: str
