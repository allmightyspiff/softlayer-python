# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createOriginPath(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping_Path]':
        data = self.client.call(
            self.service,
            'createOriginPath',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping.Path import Path
        return SL_Path(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteOriginPath(
        self,
        uniqueId: str,
        path: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'deleteOriginPath',
            uniqueId,
            path
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Mapping.Path import Path
        return SL_Path(data)

# This file was automatically generated with tools/generateTypes.py
    def listOriginPath(
        self,
        uniqueId: str
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping_Path]':
        data = self.client.call(
            self.service,
            'listOriginPath',
            uniqueId
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping.Path import Path
        return SL_Path(data)

# This file was automatically generated with tools/generateTypes.py
    def updateOriginPath(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input
    ) -> 'list[SoftLayer_Container_Network_CdnMarketplace_Configuration_Mapping_Path]':
        data = self.client.call(
            self.service,
            'updateOriginPath',
            input
        )
        from SoftLayer.datatypes.Container.Network.CdnMarketplace.Configuration.Mapping.Path import Path
        return SL_Path(data)


