from SoftLayer.sltypes.Network.Storage.Allowed.Host import Network_Storage_Allowed_Host
from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
from SoftLayer import BaseClient

class Network_Storage_Allowed_Host_IpAddress(Network_Storage_Allowed_Host):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Allowed_Host_IpAddress'

    def getObject(self, identifier: int) -> 'Network_Storage_Allowed_Host_IpAddress':
        """Retrieve a SoftLayer_Network_Storage_Allowed_Host_IpAddress record."""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_IpAddress', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Allowed_Host_IpAddress import Network_Storage_Allowed_Host_IpAddress
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_IpAddress', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getResource(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_IpAddress', 'getResource', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data
