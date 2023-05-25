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
        return data

    def deleteHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'deleteHotlinkProtection', input)
        return data

    def getHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'getHotlinkProtection', input)
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'getObject', id=identifier)
        return data

    def updateHotlinkProtection(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_HotlinkProtection', 'updateHotlinkProtection', input)
        return data
