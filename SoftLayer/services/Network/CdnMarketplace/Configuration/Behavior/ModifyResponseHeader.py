# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createModifyResponseHeader(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
    ) -> 'SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':
        data = self.client.call(
            self.service,
            'createModifyResponseHeader',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return SL_ModifyResponseHeader(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return SL_ModifyResponseHeader(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ModifyResponseHeader(data)

# This file was automatically generated with tools/generateTypes.py
    def updateModifyResponseHeader(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader]':
        data = self.client.call(
            self.service,
            'updateModifyResponseHeader',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Behavior.ModifyResponseHeader import ModifyResponseHeader
        return SL_ModifyResponseHeader(data)


