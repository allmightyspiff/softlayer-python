# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createPurge(
        self,
        uniqueId: str,
        path: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge]':
        data = self.client.call(
            self.service,
            'createPurge',
            uniqueId,
            path
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.Purge import Purge
        return SL_Purge(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Cache.Purge import Purge
        return SL_Purge(data)

# This file was automatically generated with tools/generateTypes.py
    def getPurgeHistoryPerMapping(
        self,
        uniqueId: str,
        saved: int
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge]':
        data = self.client.call(
            self.service,
            'getPurgeHistoryPerMapping',
            uniqueId,
            saved
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.Purge import Purge
        return SL_Purge(data)

# This file was automatically generated with tools/generateTypes.py
    def getPurgeStatus(
        self,
        uniqueId: str,
        path: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge]':
        data = self.client.call(
            self.service,
            'getPurgeStatus',
            uniqueId,
            path
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.Purge import Purge
        return SL_Purge(data)

# This file was automatically generated with tools/generateTypes.py
    def saveOrUnsavePurgePath(
        self,
        uniqueId: str,
        path: str,
        saveOrUnsave: int
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_Purge]':
        data = self.client.call(
            self.service,
            'saveOrUnsavePurgePath',
            uniqueId,
            path,
            saveOrUnsave
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.Purge import Purge
        return SL_Purge(data)


