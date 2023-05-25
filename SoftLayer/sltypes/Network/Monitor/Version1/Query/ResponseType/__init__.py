from SoftLayer.sltypes.Entity import Entity

class Network_Monitor_Version1_Query_ResponseType(Entity):
    """The ResponseType type stores only an ID and a description of the response type.  The only use for this object
is in reference.  The user chooses a response action that would be appropriate for a monitoring instance, and
sets the ResponseTypeId to the SoftLayer_Network_Monitor_Version1_Query_Host->responseActionId value.   The
user can retrieve all available ResponseTypes with the getAllObjects method on this service."""
    actionDescription: str
    id_: int
    level: int
