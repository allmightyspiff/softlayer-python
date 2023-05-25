from SoftLayer.sltypes.Entity import Entity

class Notification_User_Subscriber_Delivery_Method(Entity):
    """Provides mapping details of how the subscriber's notification will be delivered.  This maps the subscriber's
id with all the delivery method ids used to delivery the notification."""
    active: int
    notificationMethodId: int
    notificationUserSubscriberId: int
