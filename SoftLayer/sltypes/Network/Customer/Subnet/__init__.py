from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Customer_Subnet(Entity):
    """The SoftLayer_Network_Customer_Subnet data type contains general information relating to a single customer
subnet (remote)."""
    accountId: int
    cidr: int
    id_: int
    netmask: str
    networkIdentifier: str
    totalIpAddresses: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Customer_Subnet'

    def createObject(self, templateObject: 'Network_Customer_Subnet') -> 'Network_Customer_Subnet':
        """*"""
        data = self.client.call('SoftLayer_Network_Customer_Subnet', 'createObject', templateObject)
        return data

    def getObject(self, identifier: int) -> 'Network_Customer_Subnet':
        """Retrieve a SoftLayer_Network_Customer_Subnet record."""
        data = self.client.call('SoftLayer_Network_Customer_Subnet', 'getObject', id=identifier)
        return data

    def getIpAddresses(self, identifier: int) -> list['Network_Customer_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Network_Customer_Subnet', 'getIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Customer_Subnet_IpAddress import Network_Customer_Subnet_IpAddress
        return data
