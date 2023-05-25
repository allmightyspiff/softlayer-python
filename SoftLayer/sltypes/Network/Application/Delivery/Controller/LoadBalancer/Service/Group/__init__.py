from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Service_Group(Entity):
    id_: int
    name: str
    notes: str
    routingMethodId: int
    routingTypeId: int
    timeout: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group'

    def getGraphImage(self, identifier: int, graphType: str, metric: str) -> str:
        """Get the connection or status graph image for a load balancer service group."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getGraphImage', graphType, metric, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Service_Group':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group import Network_Application_Delivery_Controller_LoadBalancer_Service_Group
        return data

    def kickAllConnections(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'kickAllConnections', id=identifier)
        return data

    def getRoutingMethod(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Routing_Method':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getRoutingMethod', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Routing_Method import Network_Application_Delivery_Controller_LoadBalancer_Routing_Method
        return data

    def getRoutingType(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Routing_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getRoutingType', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Routing_Type import Network_Application_Delivery_Controller_LoadBalancer_Routing_Type
        return data

    def getServiceReferences(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getServiceReferences', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference import Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference
        return data

    def getServices(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getServices', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service import Network_Application_Delivery_Controller_LoadBalancer_Service
        return data

    def getVirtualServer(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_VirtualServer':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getVirtualServer', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualServer import Network_Application_Delivery_Controller_LoadBalancer_VirtualServer
        return data

    def getVirtualServers(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualServer']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service_Group', 'getVirtualServers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualServer import Network_Application_Delivery_Controller_LoadBalancer_VirtualServer
        return data
