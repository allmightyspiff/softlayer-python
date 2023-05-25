from SoftLayer.sltypes.FlexibleCredit.Enrollment import FlexibleCredit_Enrollment
from SoftLayer.sltypes.Entity import Entity

class Container_Account_Discount_Program_Collection(Entity):
    accountLevelAppliedCredit: float
    accountLevelLifetimeAppliedCredit: float
    accountLevelLifetimeCredit: float
    accountLevelLifetimeRemainingCredit: float
    accountLevelMonthlyCredit: float
    accountLevelRemainingCredit: float
    enrollments: list[FlexibleCredit_Enrollment]
    isAccountLevelParticipantFlag: bool
    isParticipantFlag: bool
    isProductSpecificParticipantFlag: bool
    productSpecificAppliedCredit: float
    productSpecificLifetimeAppliedCredit: float
    productSpecificLifetimeCredit: float
    productSpecificLifetimeRemainingCredit: float
    productSpecificMonthlyCredit: float
    productSpecificRemainingCredit: float
    totalAppliedCredit: float
    totalRemainingCredit: float
