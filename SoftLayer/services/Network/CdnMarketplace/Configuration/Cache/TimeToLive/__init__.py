# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive'
        self.client = client

    def createTimeToLive(
        self,
        uniqueId: str,
        pathName: str,
        ttl: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'createTimeToLive',
            uniqueId,
            pathName,
            ttl
        )
        
        return data


    def deleteTimeToLive(
        self,
        uniqueId: str,
        pathName: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'deleteTimeToLive',
            uniqueId,
            pathName
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Cache.TimeToLive import TimeToLive
        return TimeToLive(data)


    def listTimeToLive(
        self,
        uniqueId: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_CdnMarketplace_Configuration_Cache_TimeToLive]':

        data = self.client.call(
            self.service,
            'listTimeToLive',
            uniqueId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Cache.TimeToLive import TimeToLive
        return TimeToLive(data)


    def updateTimeToLive(
        self,
        uniqueId: str,
        oldPath: str,
        newPath: str,
        oldTtl: str,
        newTtl: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'updateTimeToLive',
            uniqueId,
            oldPath,
            newPath,
            oldTtl,
            newTtl
        )
        
        return data


