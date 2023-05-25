from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Contact(Entity):
    """Contact information container for domain registration"""
    address1: str
    address2: str
    address3: str
    city: str
    country: str
    email: str
    fax: str
    firstName: str
    lastName: str
    organizationName: str
    phone: str
    postalCode: str
    state: str
    type_: str
