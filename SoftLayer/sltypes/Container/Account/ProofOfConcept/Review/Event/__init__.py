from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Review_Event(Entity):
    """Review event within proof of concept request review period."""
    description: str
    reviewerEmail: str
    reviewerUid: str
