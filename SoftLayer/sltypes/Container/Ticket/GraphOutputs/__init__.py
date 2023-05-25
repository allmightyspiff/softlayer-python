from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Ticket_GraphOutputs(Entity):
    """SoftLayer_Container_Ticket_GraphOutputs models a single outbound object for a given bandwidth graph."""
    graphImage: str
    graphTitle: str
    maxEndDate: datetime
    minStartDate: datetime
