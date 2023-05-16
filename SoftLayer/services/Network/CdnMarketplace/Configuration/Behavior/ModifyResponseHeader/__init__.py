# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader'
        self.client = client

    def createModifyResponseHeader(
        self,
        input: 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader'
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':

        data = self.client.call(
            self.service,
            'createModifyResponseHeader',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return ModifyResponseHeader(data)


    def deleteModifyResponseHeader(
        self,
        uniqueId: str,
        modResHeaderUniqueId: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'deleteModifyResponseHeader',
            uniqueId,
            modResHeaderUniqueId
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return ModifyResponseHeader(data)


    def listModifyResponseHeader(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader]':

        data = self.client.call(
            self.service,
            'listModifyResponseHeader',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return ModifyResponseHeader(data)


    def updateModifyResponseHeader(
        self,
        input: 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader'
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader]':

        data = self.client.call(
            self.service,
            'updateModifyResponseHeader',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return ModifyResponseHeader(data)


