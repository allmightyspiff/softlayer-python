from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute(Entity):
    healthAttributeTypeId: int
    healthCheckId: int
    id_: int
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute'

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute', 'getObject', id=identifier)
        return data

    def getHealthCheck(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Check':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute', 'getHealthCheck', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Check import Network_Application_Delivery_Controller_LoadBalancer_Health_Check
        return data

    def getType(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type import Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute_Type
        return data
