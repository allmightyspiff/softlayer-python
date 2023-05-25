from SoftLayer.sltypes.Entity import Entity

class Notification_Occurrence_Resource(Entity):
    """This type contains general information relating to any hardware or services that may be impacted by a
SoftLayer_Notification_Occurrence_Event."""
    active: int
    filterLabel: str
    notificationOccurrenceEventId: int
    resourceAccountId: int
    resourceName: str
    resourceTableId: int
