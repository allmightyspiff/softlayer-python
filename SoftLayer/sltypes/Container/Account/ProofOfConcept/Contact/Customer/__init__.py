from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Contact_Customer(Entity):
    """The customer and prospective owner of a proof of concept account established by an IBMer."""
    address1: str
    address2: str
    city: str
    country: str
    email: str
    firstName: str
    lastName: str
    phone: str
    postalCode: str
    state: str
    vatId: str
