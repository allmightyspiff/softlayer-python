from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options(Entity):
    aggregatedBy: bool
    aggregatesOnly: bool
    category: str
    days: int
    endDate: datetime
    selectedStatistics: list[str]
    startDate: datetime
