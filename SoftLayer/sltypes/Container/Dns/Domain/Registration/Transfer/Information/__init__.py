from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Dns_Domain_Registration_Transfer_Information(Entity):
    """Transfer Information container for domain registration"""
    reason: str
    registrantEmail: str
    status: str
    timeStamp: datetime
    transferrable: int
