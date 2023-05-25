from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class User_Customer_Link(Entity):
    createDate: datetime
    defaultFlag: int
    destinationUserAlphanumericId: str
    destinationUserId: int
    iamIdVerificationFlag: int
    id_: int
    realm: str
    serviceProviderId: int
    uniqueIdentifier: str
    userId: int
