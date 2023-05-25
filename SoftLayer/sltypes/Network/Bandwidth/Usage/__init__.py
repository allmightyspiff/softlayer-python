from SoftLayer.sltypes.Entity import Entity

class Network_Bandwidth_Usage(Entity):
    """The SoftLayer_Network_Bandwidth_Usage data type contains specific information relating to bandwidth
utilization at a specific point in time on a given network interface."""
    amountIn: float
    amountOut: float
    bandwidthUsageDetailTypeId: float
