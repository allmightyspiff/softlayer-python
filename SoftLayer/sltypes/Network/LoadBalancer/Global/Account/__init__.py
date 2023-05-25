from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LoadBalancer_Global_Account(Entity):
    """The global load balancer service has been deprecated and is no longer available."""
    allowedNumberOfHosts: int
    averageConnectionsPerSecond: float
    connectionsPerSecond: int
    fallbackIp: str
    hostname: str
    id_: int
    loadBalanceTypeId: int
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LoadBalancer_Global_Account'

    def addNsRecord(self, identifier: int) -> bool:
        """[Deprecated] Add the required nameserver resource record for a global load balancer account."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'addNsRecord', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_LoadBalancer_Global_Account') -> bool:
        """[Deprecated] Edit a global load balancer account and the hosts that make up the load balancing pool."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_LoadBalancer_Global_Account':
        """Retrieve a SoftLayer_Network_LoadBalancer_Global_Account record."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getObject', id=identifier)
        return data

    def removeNsRecord(self, identifier: int) -> bool:
        """[Deprecated] Remove the required nameserver resource record for a global load balancer account."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'removeNsRecord', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getHosts(self, identifier: int) -> list['Network_LoadBalancer_Global_Host']:
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getHosts', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Global_Host import Network_LoadBalancer_Global_Host
        return data

    def getLoadBalanceType(self, identifier: int) -> 'Network_LoadBalancer_Global_Type':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getLoadBalanceType', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Global_Type import Network_LoadBalancer_Global_Type
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Global_Account', 'getManagedResourceFlag', id=identifier)
        return data
