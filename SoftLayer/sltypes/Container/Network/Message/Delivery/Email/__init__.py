from SoftLayer.sltypes.Entity import Entity

class Container_Network_Message_Delivery_Email(Entity):
    """This datatype is deprecated and will be removed in API version 3.2."""
    body: str
    containsHtml: bool
    from_: str
    subject: str
    to: str
