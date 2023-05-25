from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Provisioning_Version1_Transaction_History(Entity):
    finishDate: datetime
    guestId: int
    hardwareId: int
    hostId: int
    id_: int
    startDate: datetime
    transactionId: int
    transactionStatusId: int
