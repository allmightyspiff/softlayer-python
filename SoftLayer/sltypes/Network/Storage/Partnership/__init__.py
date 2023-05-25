from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Partnership(Entity):
    """A network storage partnership is used to link multiple volumes to each other. These partnerships describe
replication hierarchies or link volume snapshots to their associated storage volume."""
    createDate: datetime
    modifyDate: datetime
    partnerVolumeId: int
    volumeId: int
