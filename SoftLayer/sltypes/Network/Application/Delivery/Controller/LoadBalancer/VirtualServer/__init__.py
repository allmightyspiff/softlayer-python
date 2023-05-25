from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_VirtualServer(Entity):
    allocation: int
    id_: int
    name: str
    notes: str
    port: int
    routingMethodId: int
    virtualIpAddressId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer'

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'deleteObject', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_VirtualServer':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'getObject', id=identifier)
        return data

    def startSsl(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'startSsl', id=identifier)
        return data

    def stopSsl(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'stopSsl', id=identifier)
        return data

    def getRoutingMethod(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Routing_Method':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'getRoutingMethod', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Routing_Method import Network_Application_Delivery_Controller_LoadBalancer_Routing_Method
        return data

    def getServiceGroups(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service_Group']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'getServiceGroups', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group import Network_Application_Delivery_Controller_LoadBalancer_Service_Group
        return data

    def getVirtualIpAddress(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualServer', 'getVirtualIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
        return data
