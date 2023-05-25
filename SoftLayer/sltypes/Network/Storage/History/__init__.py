from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_History(Entity):
    """The SoftLayer_Network_Storage_History contains the username/password past history for Storage services except
Evault. Information such as the username, passwords, notes and the date of the password change may be
retrieved."""
    createDate: datetime
    notes: str
    password: str
    username: str
