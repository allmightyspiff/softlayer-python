# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createGeoblocking(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call(
            self.service,
            'createGeoblocking',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Geoblocking
        return SL_Geoblocking(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteGeoblocking(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call(
            self.service,
            'deleteGeoblocking',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Geoblocking
        return SL_Geoblocking(data)

# This file was automatically generated with tools/generateTypes.py
    def getGeoblocking(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call(
            self.service,
            'getGeoblocking',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Geoblocking
        return SL_Geoblocking(data)

# This file was automatically generated with tools/generateTypes.py
    def getGeoblockingAllowedTypesAndRegions(
        self,
        uniqueId: str
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking_Type':
        data = self.client.call(
            self.service,
            'getGeoblockingAllowedTypesAndRegions',
            uniqueId
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Geoblocking
        return SL_Geoblocking(data)

# This file was automatically generated with tools/generateTypes.py
    def updateGeoblocking(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call(
            self.service,
            'updateGeoblocking',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.Geoblocking import Geoblocking
        return SL_Geoblocking(data)


