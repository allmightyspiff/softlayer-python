from datetime import datetime
from SoftLayer.sltypes.Container.Metric.Tracking.Object.Summary import Container_Metric_Tracking_Object_Summary
from SoftLayer.sltypes.Container_Metric_Tracking_Object_Summary import Container_Metric_Tracking_Object_Summary

class Container_Metric_Tracking_Object_Virtual_Host_Summary(Container_Metric_Tracking_Object_Summary):
    """SoftLayer_Container_Metric_Tracking_Object_Virtual_Host_Summary This container summarizes a virtual host's
metric data."""
    avgMemoryUsageInBillingCycle: int
    currentBillCycleEnd: datetime
    currentBillCycleStart: datetime
    lastInstanceCount: int
    lastMemoryUsageAmount: int
    lastPollTime: datetime
    maxInstanceInBillingCycle: int
    previousBillCycleEnd: datetime
    previousBillCycleStart: datetime
    virtualPlatformName: str
