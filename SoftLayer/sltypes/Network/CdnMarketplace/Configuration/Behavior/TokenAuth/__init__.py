from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Configuration_Behavior_TokenAuth(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth'

    def createTokenAuthPath(self, input_: 'Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth') -> list['Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth']:
        """SOAP API will create Token authentication Path for an existing CDN mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth', 'createTokenAuthPath', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth import Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth
        return data

    def deleteTokenAuthPath(self, uniqueId: str, path: str) -> str:
        """SOAP API will delete token authentication Path for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth', 'deleteTokenAuthPath', uniqueId, path)
        return data

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Configuration_Behavior_TokenAuth':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth', 'getObject', id=identifier)
        return data

    def listTokenAuthPath(self, uniqueId: str) -> list['Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth']:
        """SOAP API will list token authentication paths for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth', 'listTokenAuthPath', uniqueId)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth import Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth
        return data

    def updateTokenAuthPath(self, input_: 'Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth') -> list['Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth']:
        """SOAP API will update Token authentication Path for an existing mapping and for a particular customer."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Configuration_Behavior_TokenAuth', 'updateTokenAuthPath', input)
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth import Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth
        return data
