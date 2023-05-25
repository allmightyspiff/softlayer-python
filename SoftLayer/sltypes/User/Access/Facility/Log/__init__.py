from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class User_Access_Facility_Log(Entity):
    """This class represents a login/logout sheet for facility visitors."""
    accountId: int
    description: str
    hardwareId: int
    id_: int
    locationId: int
    timeIn: datetime
    timeOut: datetime
