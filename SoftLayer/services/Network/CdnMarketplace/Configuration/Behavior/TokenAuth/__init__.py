# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth'
        self.client = client

    def createTokenAuthPath(
        self,
        input: 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth'
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth]':

        data = self.client.call(
            self.service,
            'createTokenAuthPath',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.TokenAuth import TokenAuth
        return TokenAuth(data)


    def deleteTokenAuthPath(
        self,
        uniqueId: str,
        path: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'deleteTokenAuthPath',
            uniqueId,
            path
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.TokenAuth import TokenAuth
        return TokenAuth(data)


    def listTokenAuthPath(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth]':

        data = self.client.call(
            self.service,
            'listTokenAuthPath',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.TokenAuth import TokenAuth
        return TokenAuth(data)


    def updateTokenAuthPath(
        self,
        input: 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth'
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth]':

        data = self.client.call(
            self.service,
            'updateTokenAuthPath',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.TokenAuth import TokenAuth
        return TokenAuth(data)


