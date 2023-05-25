from SoftLayer.sltypes.Entity import Entity

class Auxiliary_Notification_Emergency_Status(Entity):
    """Every SoftLayer_Auxiliary_Notification_Emergency has a statusId that references a
SoftLayer_Auxiliary_Notification_Emergency_Status data type.  The status is used to determine the current
state of the event."""
    name: str
