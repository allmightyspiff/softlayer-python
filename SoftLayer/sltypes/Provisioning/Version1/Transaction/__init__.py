from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Provisioning_Version1_Transaction(Entity):
    """The SoftLayer_Provisioning_Version1_Transaction data type contains general information relating to a single
SoftLayer hardware transaction.   SoftLayer customers are unable to change their hardware transactions."""
    createDate: datetime
    elapsedSeconds: int
    guestId: int
    hardwareId: int
    id_: int
    modifyDate: datetime
    statusChangeDate: datetime
