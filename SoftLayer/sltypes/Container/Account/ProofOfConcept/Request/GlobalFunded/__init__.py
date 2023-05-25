from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Ibmer.Technical import Container_Account_ProofOfConcept_Contact_Ibmer_Technical
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Ibmer.Requester import Container_Account_ProofOfConcept_Contact_Ibmer_Requester
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Request.Opportunity import Container_Account_ProofOfConcept_Request_Opportunity
from datetime import datetime
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Customer import Container_Account_ProofOfConcept_Contact_Customer
from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Request_GlobalFunded(Entity):
    """Proof of concept request using the global funding model. Note that proof of concept account request are
available only to internal IBM employees."""
    amount: float
    customer: Container_Account_ProofOfConcept_Contact_Customer
    description: str
    endDate: datetime
    opportunity: Container_Account_ProofOfConcept_Request_Opportunity
    projectName: str
    regionKeyName: str
    requester: Container_Account_ProofOfConcept_Contact_Ibmer_Requester
    startDate: datetime
    technicalContact: Container_Account_ProofOfConcept_Contact_Ibmer_Technical
