from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_VolumeDuplicateParameters(Entity):
    """Container for Volume Duplicate Information"""
    iopsPerGb: float
    isDuplicatable: bool
    locationId: int
    locationName: str
    maximumIopsPerGb: float
    maximumIopsTier: float
    maximumVolumeSize: int
    minimumIopsPerGb: float
    minimumIopsTier: float
    minimumVolumeSize: int
    status: str
    volumeUsername: str
