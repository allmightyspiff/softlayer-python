from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Routing_Type(Entity):
    id_: int
    keyname: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type'

    def getAllObjects(self) -> list['Network_Application_Delivery_Controller_LoadBalancer_Routing_Type']:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Routing_Type':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Routing_Type', 'getObject', id=identifier)
        return data
