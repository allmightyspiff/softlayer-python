from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Bandwidth_Projection(Entity):
    """SoftLayer_Container_Bandwidth_Projection models projected bandwidth use over a time range."""
    allowedUsage: str
    estimatedUsage: str
    hardwareId: int
    projectedUsage: str
    serverName: str
    startDate: datetime
