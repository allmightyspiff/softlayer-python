from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Ticket_Survey_Preference(Entity):
    applicable: bool
    optedOut: bool
    optedOutDate: datetime
