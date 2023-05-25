from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Info_Ach(Entity):
    accountId: int
    accountNumber: str
    accountType: str
    bankTransitNumber: str
    city: str
    country: str
    firstName: str
    id_: int
    lastName: str
    phoneNumber: str
    postalcode: str
    state: str
    status: str
    street1: str
    street2: str
    verifiedDate: datetime
