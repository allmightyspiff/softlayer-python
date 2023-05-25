from SoftLayer.sltypes.Ticket import Ticket
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Virtual_Guest_PendingMaintenanceAction(Entity):
    """The SoftLayer_Container_Virtual_Guest_PendingMaintenanceAction data type contains information relating to a
SoftLayer_Virtual_Guest's pending maintenance actions."""
    actionId: int
    dueDate: datetime
    status: str
    ticket: Ticket
    title: str
    triggerExplanation: str
