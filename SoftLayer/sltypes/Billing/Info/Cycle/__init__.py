from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Info_Cycle(Entity):
    """The SoftLayer_Billing_Info_Cycle data type models basic information concerning a SoftLayer account's previous
and current billing cycles. The information in this class is only populated for SoftLayer customers who are
billed monthly."""
    currentCycleEndDate: datetime
    currentCycleStartDate: datetime
    nextCycleStartDate: datetime
    previousCycleEndDate: datetime
    previousCycleStartDate: datetime
