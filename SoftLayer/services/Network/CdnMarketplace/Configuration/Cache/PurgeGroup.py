# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createPurgeGroup(
        self,
        uniqueId: str,
        groupName: str,
        paths: str,
        option: int
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        data = self.client.call(
            self.service,
            'createPurgeGroup',
            uniqueId,
            groupName,
            paths,
            option
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def getPurgeGroupByGroupId(
        self,
        uniqueId: str,
        groupUniqueId: str
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        data = self.client.call(
            self.service,
            'getPurgeGroupByGroupId',
            uniqueId,
            groupUniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def getPurgeGroupQuota(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getPurgeGroupQuota',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def listFavoriteGroup(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup]':
        data = self.client.call(
            self.service,
            'listFavoriteGroup',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def listUnfavoriteGroup(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup]':
        data = self.client.call(
            self.service,
            'listUnfavoriteGroup',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def purgeByGroupIds(
        self,
        uniqueId: str,
        groupUniqueIds: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory]':
        data = self.client.call(
            self.service,
            'purgeByGroupIds',
            uniqueId,
            groupUniqueIds
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroupHistory import PurgeGroupHistory
        return SL_PurgeGroupHistory(data)

# This file was automatically generated with tools/generateTypes.py
    def removePurgeGroupFromFavorite(
        self,
        uniqueId: str,
        groupUniqueId: str
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        data = self.client.call(
            self.service,
            'removePurgeGroupFromFavorite',
            uniqueId,
            groupUniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def savePurgeGroupAsFavorite(
        self,
        uniqueId: str,
        groupUniqueId: str
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        data = self.client.call(
            self.service,
            'savePurgeGroupAsFavorite',
            uniqueId,
            groupUniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Cache.PurgeGroup import PurgeGroup
        return SL_PurgeGroup(data)


