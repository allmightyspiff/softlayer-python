from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_IpAddress_Global(Entity):
    description: int
    destinationIpAddressId: int
    id_: int
    ipAddressId: int
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_IpAddress_Global'

    def getObject(self, identifier: int) -> 'Network_Subnet_IpAddress_Global':
        """Retrieve a SoftLayer_Network_Subnet_IpAddress_Global record."""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getObject', id=identifier)
        return data

    def route(self, identifier: int, newEndPointIpAddress: str) -> bool:
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'route', newEndPointIpAddress, id=identifier)
        return data

    def unroute(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'unroute', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getActiveTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item_Network_Subnet_IpAddress_Global':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Network_Subnet_IpAddress_Global import Billing_Item_Network_Subnet_IpAddress_Global
        return data

    def getDestinationIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getDestinationIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_IpAddress_Global', 'getIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data
