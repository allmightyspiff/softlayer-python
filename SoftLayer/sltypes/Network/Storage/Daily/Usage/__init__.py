from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Network_Storage_Daily_Usage(Entity):
    bytesUsed: int
    cdnHttpBandwidth: int
    createDate: datetime
    nasVolumeId: int
    publicBandwidthOut: int
