from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Review_Summary(Entity):
    """Summary presented to reviewers when determining whether or not to accept a proof of concept request. Note
that reviewers are internal IBM employees and reviews are not exposed to external users."""
    accountName: str
    accountOwnerName: str
    amount: float
    createDate: datetime
    customerEmail: str
    customerName: str
    id_: int
    lastUpdate: datetime
    nextApproverEmail: str
    requesterEmail: str
    requesterName: str
    reviewUrl: str
    status: str
