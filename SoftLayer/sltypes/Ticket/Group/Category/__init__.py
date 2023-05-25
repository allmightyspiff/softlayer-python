from SoftLayer.sltypes.Entity import Entity

class Ticket_Group_Category(Entity):
    """SoftLayer's support ticket groups represent the department at SoftLayer that is assigned to work one of your
support tickets. Many departments are responsible for handling different types of tickets. These types of
tickets are modeled in the SoftLayer_Ticket_Group_Category data type. Ticket group categories also help
separate differentiate your tickets' issues in the SoftLayer customer portal."""
    id_: int
    name: str
