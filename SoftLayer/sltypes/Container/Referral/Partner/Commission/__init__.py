from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Referral_Partner_Commission(Entity):
    commissionAmount: float
    commissionRate: float
    createDate: datetime
    referralAccountId: int
    referralCompanyName: str
    referralPartnerAccountId: int
    referralRevenue: float
