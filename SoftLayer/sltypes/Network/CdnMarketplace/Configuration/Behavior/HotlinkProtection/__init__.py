from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection(Entity):
    protectionType: str
    refererValues: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection'

    def createHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'createHotlinkProtection', input)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
        return data

    def deleteHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'deleteHotlinkProtection', input)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
        return data

    def getHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'getHotlinkProtection', input)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
        return data

    def updateHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'updateHotlinkProtection', input)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection import Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection
        return data
