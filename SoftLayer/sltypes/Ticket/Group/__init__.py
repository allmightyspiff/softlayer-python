from SoftLayer.sltypes.Entity import Entity

class Ticket_Group(Entity):
    """SoftLayer tickets have the ability to be assigned to one of SoftLayer's internal departments. The department
that a ticket is assigned to is modeled by the SoftLayer_Ticket_Group data type. Ticket groups help to ensure
that the proper department is handling a ticket. Standard support tickets are created from a number of pre-
determined subjects. These subjects help determine which group a standard ticket is assigned to."""
    id_: int
    name: str
    ticketGroupCategoryId: int
