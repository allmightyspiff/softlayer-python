from SoftLayer.sltypes.Entity import Entity

class Notification_Delivery_Method(Entity):
    """Provides details for the delivery methods available."""
    active: int
    description: str
    id_: int
    keyName: str
    name: str
