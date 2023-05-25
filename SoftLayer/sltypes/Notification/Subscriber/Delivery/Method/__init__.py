from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Notification_Subscriber_Delivery_Method(Entity):
    """Provides details for the subscriber's delivery methods."""
    active: int
    createDate: datetime
    modifyDate: datetime
    notificationDeliveryMethodId: int
    notificationSubscriberId: int
