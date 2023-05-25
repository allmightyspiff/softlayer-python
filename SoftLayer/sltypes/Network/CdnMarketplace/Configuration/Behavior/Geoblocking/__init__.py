from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Behavior_Geoblocking(Entity):
    accessType: str
    regionType: str
    regions: list[str]
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking'

    def createGeoblocking(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'createGeoblocking', input)
        return data

    def deleteGeoblocking(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'deleteGeoblocking', input)
        return data

    def getGeoblocking(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'getGeoblocking', input)
        return data

    def getGeoblockingAllowedTypesAndRegions(self, uniqueId: str) -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking_Type':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'getGeoblockingAllowedTypesAndRegions', uniqueId)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_Geoblocking_Type import Network_CdnMarketplace_Configuration_Behavior_Geoblocking_Type
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'getObject', id=identifier)
        return data

    def updateGeoblocking(self, input_: 'Container_Network_CdnMarketplace_Configuration_Input') -> 'Network_CdnMarketplace_Configuration_Behavior_Geoblocking':
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_Geoblocking', 'updateGeoblocking', input)
        return data
