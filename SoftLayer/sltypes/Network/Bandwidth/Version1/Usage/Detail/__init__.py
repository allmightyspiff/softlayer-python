from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Bandwidth_Version1_Usage_Detail(Entity):
    """The SoftLayer_Network_Bandwidth_Version1_Usage_Detail data type contains specific information relating to
bandwidth utilization at a specific point in time on a given network interface."""
    amountIn: float
    amountOut: float
    day: datetime
