from SoftLayer.sltypes.Entity import Entity

class Ticket_State(Entity):
    id_: int
    stateTypeId: int
    ticketId: int
