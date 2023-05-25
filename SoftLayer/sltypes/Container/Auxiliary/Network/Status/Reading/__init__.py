from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Auxiliary_Network_Status_Reading(Entity):
    averagePing: float
    fails: int
    frequency: int
    label: str
    lastCheckDate: datetime
    lastDownDate: datetime
    latency: float
    location: str
    maximumPing: float
    minimumPing: float
    pingLoss: float
    startDate: datetime
    statusCode: str
    statusMessage: str
    target: str
    targetType: str
