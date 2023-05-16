# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection'
        self.client = client

    def createHotlinkProtection(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':

        data = self.client.call(
            self.service,
            'createHotlinkProtection',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import HotlinkProtection
        return HotlinkProtection(data)


    def deleteHotlinkProtection(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':

        data = self.client.call(
            self.service,
            'deleteHotlinkProtection',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import HotlinkProtection
        return HotlinkProtection(data)


    def getHotlinkProtection(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':

        data = self.client.call(
            self.service,
            'getHotlinkProtection',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import HotlinkProtection
        return HotlinkProtection(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import HotlinkProtection
        return HotlinkProtection(data)


    def updateHotlinkProtection(
        self,
        input: SoftLayer_Container_Network_CdnMarketplace_Configuration_Input,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':

        data = self.client.call(
            self.service,
            'updateHotlinkProtection',
            input,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.CdnMarketplace.Configuration.Behavior.HotlinkProtection import HotlinkProtection
        return HotlinkProtection(data)


