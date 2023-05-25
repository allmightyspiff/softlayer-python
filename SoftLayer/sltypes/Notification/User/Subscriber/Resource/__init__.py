from SoftLayer.sltypes.Entity import Entity

class Notification_User_Subscriber_Resource(Entity):
    """Retrieve identifier cross-reference information.  SoftLayer_Notification_User_Subscriber_Resource provides
the resource table id and subscriber id relation. The resource table id is the id of the service the
subscriber receives alerts for.  This resource table id could be the unique identifier for a Storage Evault
service or CDN service."""
    notificationUserSubscriberId: int
    resourceTableId: int
