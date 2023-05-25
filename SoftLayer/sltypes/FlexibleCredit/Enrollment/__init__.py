from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class FlexibleCredit_Enrollment(Entity):
    accountId: int
    affiliateId: int
    agreementCompleteFlag: int
    companyDescription: str
    companyTypeId: int
    enrollmentDate: datetime
    graduationDate: datetime
    monthlyCreditAmount: float
    representativeEmployeeId: int
