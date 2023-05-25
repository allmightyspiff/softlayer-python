from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Account_PersonalInformation(Entity):
    accountId: int
    address1: str
    address2: str
    alternatePhone: str
    city: str
    country: str
    email: str
    firstName: str
    lastName: str
    officePhone: str
    postalCode: str
    requestDate: datetime
    requestId: int
    state: str
