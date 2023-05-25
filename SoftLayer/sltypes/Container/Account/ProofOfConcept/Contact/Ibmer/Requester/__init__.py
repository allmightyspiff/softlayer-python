from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Contact_Ibmer_Requester(Entity):
    """IBMer who is submitting a proof of concept request on behalf of a prospective customer."""
    address1: str
    address2: str
    businessUnit: str
    city: str
    country: str
    email: str
    firstName: str
    lastName: str
    organizationCountry: str
    paasAccountId: str
    phone: str
    postalCode: str
    state: str
    subOrganization: str
    uid: str
    vatId: str
