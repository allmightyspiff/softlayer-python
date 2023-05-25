from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Notification_Subscriber(Entity):
    active: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    notificationId: int
    notificationSubscriberTypeId: int
    notificationSubscriberTypeResourceId: int
