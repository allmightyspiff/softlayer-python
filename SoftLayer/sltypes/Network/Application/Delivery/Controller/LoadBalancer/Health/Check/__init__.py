from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Health_Check(Entity):
    healthCheckTypeId: int
    id_: int
    name: str
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check'

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Check':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check', 'getObject', id=identifier)
        return data

    def getAttributes(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute import Network_Application_Delivery_Controller_LoadBalancer_Health_Attribute
        return data

    def getServices(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check', 'getServices', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service import Network_Application_Delivery_Controller_LoadBalancer_Service
        return data

    def getType(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Health_Check', 'getType', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type import Network_Application_Delivery_Controller_LoadBalancer_Health_Check_Type
        return data
