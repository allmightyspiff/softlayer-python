from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_Bandwidth_Version1_Usage(Entity):
    """SoftLayer_Container_Network_Bandwidth_Version1_Usage models an hourly bandwidth record."""
    incomingAmount: float
    outgoingAmount: float
    recordedDate: datetime
