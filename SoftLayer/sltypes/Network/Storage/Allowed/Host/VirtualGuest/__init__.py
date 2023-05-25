from SoftLayer.sltypes.Network.Storage.Allowed.Host import Network_Storage_Allowed_Host
from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
from SoftLayer import BaseClient

class Network_Storage_Allowed_Host_VirtualGuest(Network_Storage_Allowed_Host):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Allowed_Host_VirtualGuest'

    def getObject(self, identifier: int) -> 'Network_Storage_Allowed_Host_VirtualGuest':
        """Retrieve a SoftLayer_Network_Storage_Allowed_Host_VirtualGuest record."""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_VirtualGuest', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_VirtualGuest', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getResource(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_VirtualGuest', 'getResource', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
