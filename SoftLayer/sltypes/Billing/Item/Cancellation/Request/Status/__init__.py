from SoftLayer.sltypes.Entity import Entity

class Billing_Item_Cancellation_Request_Status(Entity):
    """SoftLayer_Billing_Item_Cancellation_Request_Status data type represents the status of a service cancellation
request."""
    description: str
    id_: int
    keyName: str
    name: str
