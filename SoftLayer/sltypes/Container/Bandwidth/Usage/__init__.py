from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Bandwidth_Usage(Entity):
    """When a customer uses SoftLayer_Account::getBandwidthUsage, this container is used to return their usage
information in bytes"""
    endDate: datetime
    hardwareId: int
    privateInUsage: float
    privateOutUsage: float
    publicInUsage: float
    publicOutUsage: float
    startDate: datetime
