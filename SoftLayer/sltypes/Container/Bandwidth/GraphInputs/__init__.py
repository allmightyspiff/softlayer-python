from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Bandwidth_GraphInputs(Entity):
    """SoftLayer_Container_Bandwidth_GraphInputs models a single inbound object for a given bandwidth graph."""
    endDate: datetime
    networkInterfaceId: int
    pod: int
    serverName: str
    startDate: datetime
