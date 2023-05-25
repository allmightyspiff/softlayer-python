from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Cache_Purge(Entity):
    """This data type models a purge event that occurs in caching server. It contains a reference to a mapping
configuration, the path to execute the purge on, the status of the purge, and flag that enables saving the
purge information for future use."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge'

    def createPurge(self, uniqueId: str, path: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_Purge']:
        """This method creates a purge record in the purge table, and also initiates the create purge call."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge', 'createPurge', uniqueId, path)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_Purge import Container_Network_CdnMarketplace_Configuration_Cache_Purge
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Cache_Purge':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Cache_Purge import Network_CdnMarketplace_Configuration_Cache_Purge
        return data

    def getPurgeHistoryPerMapping(self, uniqueId: str, saved: int) -> list['Container_Network_CdnMarketplace_Configuration_Cache_Purge']:
        """This method returns the purge history for a given domain and CDN account."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge', 'getPurgeHistoryPerMapping', uniqueId, saved)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_Purge import Container_Network_CdnMarketplace_Configuration_Cache_Purge
        return data

    def getPurgeStatus(self, uniqueId: str, path: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_Purge']:
        """This method gets the status of a given purge path."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge', 'getPurgeStatus', uniqueId, path)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_Purge import Container_Network_CdnMarketplace_Configuration_Cache_Purge
        return data

    def saveOrUnsavePurgePath(self, uniqueId: str, path: str, saveOrUnsave: int) -> list['Container_Network_CdnMarketplace_Configuration_Cache_Purge']:
        """Creates a new saved purge if a purge path is saved. Deletes a saved purge record if the path is unsaved."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge', 'saveOrUnsavePurgePath', uniqueId, path, saveOrUnsave)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_Purge import Container_Network_CdnMarketplace_Configuration_Cache_Purge
        return data
