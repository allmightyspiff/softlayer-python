# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Cache.PurgeHistory import PurgeHistory
        return SL_PurgeHistory(data)

# This file was automatically generated with tools/generateTypes.py
    def listPurgeGroupHistory(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory]':
        data = self.client.call(
            self.service,
            'listPurgeGroupHistory',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroupHistory import PurgeGroupHistory
        return SL_PurgeGroupHistory(data)


