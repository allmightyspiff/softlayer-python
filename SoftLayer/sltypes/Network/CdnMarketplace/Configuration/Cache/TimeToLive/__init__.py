from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Cache_TimeToLive(Entity):
    """This data type models a purge event that occurs repetitively and automatically in caching server after a set
interval of time. A time to live instance contains a reference to a mapping configuration, the path to
execute the purge on, the result of the purge, and the time interval after which the purge will be executed."""
    createDate: datetime
    path: str
    timeToLive: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive'

    def createTimeToLive(self, uniqueId: str, pathName: str, ttl: str) -> str:
        """Creates a Time To Live object and inserts it into the database"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive', 'createTimeToLive', uniqueId, pathName, ttl)
        return data

    def deleteTimeToLive(self, uniqueId: str, pathName: str) -> str:
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive', 'deleteTimeToLive', uniqueId, pathName)
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Cache_TimeToLive':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive', 'getObject', id=identifier)
        return data

    def listTimeToLive(self, uniqueId: str) -> list['Network_CdnMarketplace_Configuration_Cache_TimeToLive']:
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive', 'listTimeToLive', uniqueId)
        return data

    def updateTimeToLive(self, uniqueId: str, oldPath: str, newPath: str, oldTtl: str, newTtl: str) -> str:
        """Updates an existing Time To Live object. If the old and new inputs are equal, exits early."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive', 'updateTimeToLive', uniqueId, oldPath, newPath, oldTtl, newTtl)
        return data
