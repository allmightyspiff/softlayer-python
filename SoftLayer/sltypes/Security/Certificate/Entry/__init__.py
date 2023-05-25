from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Security_Certificate_Entry(Entity):
    certificateId: int
    commonName: str
    keySize: int
    organizationName: str
    validityBegin: datetime
    validityDays: int
    validityEnd: datetime
