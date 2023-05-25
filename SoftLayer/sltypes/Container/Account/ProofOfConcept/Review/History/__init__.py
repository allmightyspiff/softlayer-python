from SoftLayer.sltypes.Container.Account.ProofOfConcept.Review.Event import Container_Account_ProofOfConcept_Review_Event
from SoftLayer.sltypes.Entity import Entity

class Container_Account_ProofOfConcept_Review_History(Entity):
    """Summary of review activity for a proof of concept request."""
    accountCreatedFlag: bool
    deniedFlag: bool
    events: list[Container_Account_ProofOfConcept_Review_Event]
    reviewCompleteFlag: bool
