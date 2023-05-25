from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Ibmer.Technical import Container_Account_ProofOfConcept_Contact_Ibmer_Technical
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Review.History import Container_Account_ProofOfConcept_Review_History
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Ibmer.Requester import Container_Account_ProofOfConcept_Contact_Ibmer_Requester
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Request.Opportunity import Container_Account_ProofOfConcept_Request_Opportunity
from datetime import datetime
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Contact.Customer import Container_Account_ProofOfConcept_Contact_Customer
from SoftLayer.sltypes.Container.Account.ProofOfConcept.Request.CostRecovery import Container_Account_ProofOfConcept_Request_CostRecovery
from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Review(Entity):
    """Full details presented to reviewers when determining whether or not to accept a proof of concept request.
Note that reviewers are internal IBM employees and reviews are not exposed to external users."""
    accountType: str
    costRecoveryCodes: Container_Account_ProofOfConcept_Request_CostRecovery
    customer: Container_Account_ProofOfConcept_Contact_Customer
    description: str
    endDate: datetime
    fundingAmount: float
    fundingType: str
    id_: int
    iotLeadName: str
    iotRegionName: str
    managerName: str
    opportunity: Container_Account_ProofOfConcept_Request_Opportunity
    projectName: str
    requester: Container_Account_ProofOfConcept_Contact_Ibmer_Requester
    reviewHistory: Container_Account_ProofOfConcept_Review_History
    reviewUrl: str
    startDate: datetime
    technicalContact: Container_Account_ProofOfConcept_Contact_Ibmer_Technical
