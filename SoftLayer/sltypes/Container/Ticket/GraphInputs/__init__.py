from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Ticket_GraphInputs(Entity):
    """SoftLayer_Container_Ticket_GraphInputs models a single inbound object for a given ticket graph."""
    endDate: datetime
    networkInterfaceId: int
    pod: int
    serverName: str
    startDate: datetime
