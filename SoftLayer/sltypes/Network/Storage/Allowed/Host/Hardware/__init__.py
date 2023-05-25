from SoftLayer.sltypes.Network.Storage.Allowed.Host import Network_Storage_Allowed_Host
from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
from SoftLayer import BaseClient

class Network_Storage_Allowed_Host_Hardware(Network_Storage_Allowed_Host):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Allowed_Host_Hardware'

    def getObject(self, identifier: int) -> 'Network_Storage_Allowed_Host_Hardware':
        """Retrieve a SoftLayer_Network_Storage_Allowed_Host_Hardware record."""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Hardware', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host_Hardware import Network_Storage_Allowed_Host_Hardware
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Hardware', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getResource(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Hardware', 'getResource', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data
