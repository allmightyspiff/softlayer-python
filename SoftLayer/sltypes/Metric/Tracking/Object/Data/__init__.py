from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Metric_Tracking_Object_Data(Entity):
    """SoftLayer_Metric_Tracking_Object_Data models an individual unit of data tracked by a SoftLayer tracking
object, including the type of data polled, the date it was polled at, and the counter value that was measured
at polling time."""
    counter: float
    dateTime: datetime
    type_: str
