from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Billing_Item_Cancellation_Request_Item(Entity):
    """SoftLayer_Billing_Item_Cancellation_Request_Item data type contains a billing item for cancellation. This
data type is used to harness billing items to the associated service."""
    billingItemId: int
    cancellationRequestId: int
    id_: int
    immediateCancellationFlag: bool
    scheduledCancellationDate: datetime
    serviceReclaimStatusCode: str
