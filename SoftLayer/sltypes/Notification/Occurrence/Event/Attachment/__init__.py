from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Notification_Occurrence_Event_Attachment(Entity):
    """SoftLayer events can have have files attached to them by a SoftLayer employee. Attaching a file to a event is
a way to provide supplementary information such as a RFO (reason for outage) document or root cause analysis.
The SoftLayer_Notification_Occurrence_Event_Attachment data type models a single file attached to a event."""
    createDate: datetime
    fileName: str
    fileSize: str
    id_: int
    notificationOccurrenceEventId: int
