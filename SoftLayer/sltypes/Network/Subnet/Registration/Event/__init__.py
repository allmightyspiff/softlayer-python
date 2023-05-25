from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Subnet_Registration_Event(Entity):
    """Each time a [[SoftLayer_Network_Subnet_Registration|subnet registration]] object is created or modified, the
system will generate an event for it. Additional actions that would create an event include RIR responses and
error cases. *"""
    createDate: datetime
    id_: int
    message: str
    modifyDate: datetime
    registrationId: int
    typeId: int
