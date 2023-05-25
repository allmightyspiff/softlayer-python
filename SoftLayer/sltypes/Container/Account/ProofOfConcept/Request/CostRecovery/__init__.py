from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Request_CostRecovery(Entity):
    """Funding codes for the department paying for the proof of concept account."""
    countryCode: str
    departmentCode: str
    divisionCode: str
