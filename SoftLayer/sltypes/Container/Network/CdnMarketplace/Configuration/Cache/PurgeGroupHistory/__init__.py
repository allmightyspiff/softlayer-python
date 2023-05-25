from datetime import datetime
from SoftLayer.sltypes.Entity import Entity

class Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory(Entity):
    """The SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory data type contains
information for specific responses from the Purge Group API and Purge History API."""
    createDate: datetime
    groupName: str
    groupUniqueId: str
    status: str
    uniqueId: str
