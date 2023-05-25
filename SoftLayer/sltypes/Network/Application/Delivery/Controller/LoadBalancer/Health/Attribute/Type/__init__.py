from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type(Entity):
    description: str
    id_: int
    keyname: str
    name: str
    valueExpression: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type'

    def getAllObjects(self) -> list['Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type']:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type', 'getObject', id=identifier)
        return data
