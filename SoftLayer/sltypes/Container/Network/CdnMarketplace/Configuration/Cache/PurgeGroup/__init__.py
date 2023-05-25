from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup(Entity):
    """The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup data type contains information
for specific responses from the Purge Group API. Each of the Purge Group APIs returns a collection of this
type"""
    createDate: datetime
    groupUniqueId: str
    lastPurgeDate: datetime
    name: str
    option: int
    pathCount: int
    paths: list[str]
    purgeStatus: str
    saved: str
    uniqueId: str
