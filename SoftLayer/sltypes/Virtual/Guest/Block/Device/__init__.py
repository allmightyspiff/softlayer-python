from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Virtual_Guest_Block_Device(Entity):
    """The block device data type presents the structure in which all block devices will be presented. A block
device attaches a disk image to a guest. Internally, the structure supports various virtualization platforms
with no change to external interaction.   A guest, also known as a virtual server, represents an allocation
of resources on a virtual host."""
    bootableFlag: int
    createDate: datetime
    device: str
    diskImageId: int
    guestId: int
    hotPlugFlag: int
    id_: int
    modifyDate: datetime
    mountMode: str
    mountType: str
    statusId: int
    uuid: str
