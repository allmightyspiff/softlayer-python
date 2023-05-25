from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Software_Component_Password_History(Entity):
    """This object allows you to find the history of password changes for a specific SoftLayer_Software Component"""
    createDate: datetime
    notes: str
    password: str
    softwareComponentId: int
    username: str
