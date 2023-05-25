from SoftLayer.sltypes.Entity import Entity

class Location_Status(Entity):
    """SoftLayer_Location_Status models the state of any location. SoftLayer uses the following status codes:
*'''ACTIVE''': The location is currently active and available for public usage. *'''PLANNED''': Used when a
location is planned but not yet active. *'''RETIRED''': Used when a location has been retired and no longer
active.   Locations in use should stay in the ACTIVE state. If a locations status ever reads anything else
and contains active hardware then please contact SoftLayer support."""
    id_: int
    status: str
