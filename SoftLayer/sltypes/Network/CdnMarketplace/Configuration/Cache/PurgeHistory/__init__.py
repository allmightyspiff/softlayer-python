from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Cache_PurgeHistory(Entity):
    """This data type models a purge history event that occurs in caching server. The purge group history will be
deleted after 15 days. The possible purge status of each history can be 'SUCCESS', "FAILED" or "IN_PROGRESS"."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory'

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Cache_PurgeHistory':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Cache_PurgeHistory import Network_CdnMarketplace_Configuration_Cache_PurgeHistory
        return data

    def listPurgeGroupHistory(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory']:
        """This method returns the list of purge group histories"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_PurgeHistory', 'listPurgeGroupHistory', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory import Container_Network_CdnMarketplace_Configuration_Cache_PurgeGroupHistory
        return data
