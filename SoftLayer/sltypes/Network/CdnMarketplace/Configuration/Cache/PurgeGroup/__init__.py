from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Cache_PurgeGroup(Entity):
    """This data type models a purge group event that occurs in caching server. It contains a reference to a mapping
configuration and the path to execute the purge on."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup'

    def createPurgeGroup(self, uniqueId: str, groupName: str, paths: str, option: int) -> 'Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        """This method creates a purge group record in the table, and also initiates the purge action based on the input
option value. The unsaved groups will be deleted after 15 days if no purge actions executed. The possible
input option value can be: 1: (Default) Only purge the paths in the group, don't save the group as favorite.
2: Only save the group as favorite, don't purge the paths. 3: Save the group as favorite and also purge the
paths in the group."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'createPurgeGroup', uniqueId, groupName, paths, option)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'getObject', id=identifier)
        return data

    def getPurgeGroupByGroupId(self, uniqueId: str, groupUniqueId: str) -> 'Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        """This method returns the purge group for a given domain and group ID."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'getPurgeGroupByGroupId', uniqueId, groupUniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data

    def getPurgeGroupQuota(self) -> int:
        """This method gets a purge group quota."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'getPurgeGroupQuota')
        return data

    def listFavoriteGroup(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup']:
        """This method returns the list of favorite purge groups."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'listFavoriteGroup', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data

    def listUnfavoriteGroup(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup']:
        """This method returns the list of unsaved purge groups."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'listUnfavoriteGroup', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data

    def purgeByGroupIds(self, uniqueId: str, groupUniqueIds: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory']:
        """This method purges the content from purge groups."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'purgeByGroupIds', uniqueId, groupUniqueIds)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory
        return data

    def removePurgeGroupFromFavorite(self, uniqueId: str, groupUniqueId: str) -> 'Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        """This method removes a purge group from favorite."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'removePurgeGroupFromFavorite', uniqueId, groupUniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data

    def savePurgeGroupAsFavorite(self, uniqueId: str, groupUniqueId: str) -> 'Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup':
        """This method saves a purge group as favorite."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeGroup', 'savePurgeGroupAsFavorite', uniqueId, groupUniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroup
        return data
