from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Account_Link(Entity):
    accountId: int
    authorizationToken: str
    createDate: datetime
    destinationAccountAlphanumericId: str
    destinationAccountId: int
    id_: int
    serviceProviderId: int
