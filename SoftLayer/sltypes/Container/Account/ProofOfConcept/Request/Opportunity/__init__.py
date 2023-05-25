from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Request_Opportunity(Entity):
    """Internal IBM opportunity codes required when applying for a Proof of Concept account."""
    campaignCode: str
    monthlyRecurringRevenue: float
    opportunityNumber: str
    totalContractValue: float
