from SoftLayer.sltypes.Network.Storage.Allowed.Host import Network_Storage_Allowed_Host
from SoftLayer.sltypes.Network_Storage_Allowed_Host import Network_Storage_Allowed_Host
from SoftLayer import BaseClient

class Network_Storage_Allowed_Host_Subnet(Network_Storage_Allowed_Host):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Allowed_Host_Subnet'

    def getObject(self, identifier: int) -> 'Network_Storage_Allowed_Host_Subnet':
        """Retrieve a SoftLayer_Network_Storage_Allowed_Host_Subnet record."""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Subnet', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Subnet', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getResource(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host_Subnet', 'getResource', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
