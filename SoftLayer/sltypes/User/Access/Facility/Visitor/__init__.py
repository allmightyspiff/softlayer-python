from SoftLayer.sltypes.Entity import Entity

class User_Access_Facility_Visitor(Entity):
    """This class represents a facility visitor that is not an active employee or customer."""
    companyName: str
    firstName: str
    lastName: str
    typeId: int
