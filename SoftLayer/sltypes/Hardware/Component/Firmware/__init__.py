from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Firmware(Entity):
    buildDate: datetime
    createDate: datetime
    hardwareComponentModelId: int
    id_: int
    isQualified: int
    releaseNotes: str
    severity: int
    version: str
