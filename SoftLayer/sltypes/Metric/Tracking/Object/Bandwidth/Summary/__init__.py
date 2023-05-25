from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Metric_Tracking_Object_Bandwidth_Summary(Entity):
    """This data type provides commonly used bandwidth summary components for the current billing cycle."""
    allocationAmount: float
    allocationId: int
    amountOut: float
    averageDailyUsage: float
    currentlyOverAllocationFlag: int
    id_: int
    inboundBandwidthAmount: float
    outboundBandwidthAmount: float
    projectedBandwidthUsage: float
    projectedOverAllocationFlag: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Metric_Tracking_Object_Bandwidth_Summary'

    def getObject(self, identifier: int) -> 'Metric_Tracking_Object_Bandwidth_Summary':
        """Retrieve a SoftLayer_Metric_Tracking_Object_Bandwidth_Summary record."""
        data = self.client.call('SoftLayer_Metric_Tracking_Object_Bandwidth_Summary', 'getObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object_Bandwidth_Summary import Metric_Tracking_Object_Bandwidth_Summary
        return data
