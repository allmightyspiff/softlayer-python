from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Account_Discount_Program(Entity):
    """SoftLayer_Container_Account_Discount_Program models a single outbound object for a graph of given data sets."""
    appliedCredit: float
    isParticipant: bool
    lifetimeAppliedCredit: float
    lifetimeCredit: float
    lifetimeRemainingCredit: float
    maximumActiveOrders: float
    monthlyCredit: float
    postTaxRemainingCredit: float
    programEndDate: datetime
    programName: str
    remainingCredit: float
    remainingCreditTax: float
