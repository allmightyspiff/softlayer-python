from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Hardware_Component(Entity):
    """The SoftLayer_Hardware_Component data type abstracts information related to a hardware component."""
    hardwareComponentModelId: int
    hardwareId: int
    id_: int
    modifyDate: datetime
    name: str
    serialNumber: str
    serviceProviderId: int
