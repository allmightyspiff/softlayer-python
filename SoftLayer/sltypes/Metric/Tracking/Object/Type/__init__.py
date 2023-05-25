from SoftLayer.sltypes.Entity import Entity

class Metric_Tracking_Object_Type(Entity):
    """SoftLayer [[SoftLayer_Metric_Tracking_Object|tracking objects]] can model various kinds of measured data,
from server and virtual server bandwidth usage to CPU use to remote storage usage.
SoftLayer_Metric_Tracking_Object_Type models one of these types and is referred to in tracking objects to
reflect what type of data they track."""
    keyname: str
    name: str
