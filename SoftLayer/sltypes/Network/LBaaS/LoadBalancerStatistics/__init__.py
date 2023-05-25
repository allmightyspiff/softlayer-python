from SoftLayer.sltypes.Entity import Entity

class Network_LBaaS_LoadBalancerStatistics(Entity):
    """SoftLayer_Network_LBaaS_LoadBalancerStatistics is a collection of metrics retrieved from a load balancer
instance. The available metrics are: <ul> <li>NUmber of members up</li> <li>Number of members down</li>
<li>Total number of active connections</li> <li>Throughput</li> <li>Data processed by month</li>
<li>Connection rate</li> </ul>"""
    connectionRate: int
    dataProcessedByMonth: int
    numberOfMembersDown: int
    numberOfMembersUp: int
    throughput: float
    totalConnections: int
