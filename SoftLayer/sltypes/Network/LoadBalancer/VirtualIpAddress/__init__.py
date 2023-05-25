from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LoadBalancer_VirtualIpAddress(Entity):
    """The SoftLayer_Network_LoadBalancer_VirtualIpAddress data type contains all the information relating to a
specific load balancer assigned to a customer account.   Information retained on the object itself is the
virtual IP address, load balancing method, and any notes that are related to the load balancer.  There is
also an array of SoftLayer_Network_LoadBalancer_Service objects, which represent the load balancer services,
explained more fully in the SoftLayer_Network_LoadBalancer_Service documentation."""
    connectionLimit: int
    id_: int
    loadBalancingMethod: str
    loadBalancingMethodFullName: str
    modifyDate: datetime
    name: str
    notes: str
    securityCertificateId: int
    sourcePort: int
    type_: str
    virtualIpAddress: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LoadBalancer_VirtualIpAddress'

    def disable(self, identifier: int) -> bool:
        """Disable a Virtual IP Address"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'disable', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_LoadBalancer_VirtualIpAddress') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'editObject', templateObject, id=identifier)
        return data

    def enable(self, identifier: int) -> bool:
        """Enable a Virtual IP Address"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'enable', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_LoadBalancer_VirtualIpAddress':
        """Retrieve a SoftLayer_Network_LoadBalancer_VirtualIpAddress record."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getObject', id=identifier)
        return data

    def kickAllConnections(self, identifier: int) -> bool:
        """Kick all active connections off a Virtual IP Address."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'kickAllConnections', id=identifier)
        return data

    def upgradeConnectionLimit(self, identifier: int) -> bool:
        """Upgrades the connection limit on the Virtual IP Address and changes the billing item on your account to
reflect the change."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'upgradeConnectionLimit', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCustomerManagedFlag(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getCustomerManagedFlag', id=identifier)
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getManagedResourceFlag', id=identifier)
        return data

    def getServices(self, identifier: int) -> list['Network_LoadBalancer_Service']:
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_VirtualIpAddress', 'getServices', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Service import Network_LoadBalancer_Service
        return data
