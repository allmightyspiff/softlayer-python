from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_LoadBalancerMonitoringMetricDataPoint(Entity):
    """SoftLayer_Network_LBaaS_LoadBalancerMonitoringMetricDataPoint is a collection of datapoints retrieved from a
load balancer instance. The available metrics are: <ul> <li>The metric value </li> <li>The timestamp when the
metric value was obtained </li> </ul>"""
    epochTimestamp: int
    value: float
