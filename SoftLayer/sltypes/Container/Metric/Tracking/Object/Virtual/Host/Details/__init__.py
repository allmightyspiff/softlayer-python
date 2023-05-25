from datetime import datetime
from SoftLayer.sltypes.Container.Metric.Tracking.Object.Details import Container_Metric_Tracking_Object_Details
from SoftLayer.sltypes.Container_Metric_Tracking_Object_Details import Container_Metric_Tracking_Object_Details

class Container_Metric_Tracking_Object_Virtual_Host_Details(Container_Metric_Tracking_Object_Details):
    """SoftLayer_Container_Metric_Tracking_Object_Virtual_Host_Details This container details a virtual host's
metric data."""
    day: datetime
    maxInstances: int
    maxMemoryUsage: int
    meanInstances: float
    meanMemoryUsage: float
    minInstances: int
    minMemoryUsage: int
