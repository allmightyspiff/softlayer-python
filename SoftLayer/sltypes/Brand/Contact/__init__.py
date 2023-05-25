from SoftLayer.sltypes.Entity import Entity

class Brand_Contact(Entity):
    """SoftLayer_Brand_Contact contains the contact information for the brand such as Corporate or Support contact
information"""
    address1: str
    address2: str
    alternatePhone: str
    brandContactTypeId: int
    city: str
    country: str
    email: str
    faxPhone: str
    firstName: str
    lastName: str
    officePhone: str
    postalCode: str
    state: str
