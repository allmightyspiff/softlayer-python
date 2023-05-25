from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Notification_Occurrence_Update(Entity):
    contents: str
    createDate: datetime
    endDate: datetime
    startDate: datetime
