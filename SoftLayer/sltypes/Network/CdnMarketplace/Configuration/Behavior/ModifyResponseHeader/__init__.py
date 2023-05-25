from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader'

    def createModifyResponseHeader(self, input_: 'Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader') -> 'Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':
        """SOAP API will create modify response header for an existing CDN mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader', 'createModifyResponseHeader', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader import Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
        return data

    def deleteModifyResponseHeader(self, uniqueId: str, modResHeaderUniqueId: str) -> str:
        """SOAP API will delete modify response header for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader', 'deleteModifyResponseHeader', uniqueId, modResHeaderUniqueId)
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader import Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
        return data

    def listModifyResponseHeader(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader']:
        """SOAP API will list modify response headers for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader', 'listModifyResponseHeader', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader import Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
        return data

    def updateModifyResponseHeader(self, input_: 'Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader') -> list['Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader']:
        """SOAP API will update modify response header for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader', 'updateModifyResponseHeader', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader import Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
        return data
