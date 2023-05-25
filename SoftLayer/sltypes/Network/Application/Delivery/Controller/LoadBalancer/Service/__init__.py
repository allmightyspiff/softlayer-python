from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_LoadBalancer_Service(Entity):
    enabled: int
    id_: int
    ipAddressId: int
    name: str
    notes: str
    port: int
    status: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service'

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'deleteObject', id=identifier)
        return data

    def getGraphImage(self, identifier: int, graphType: str, metric: str) -> str:
        """Get the connection or status graph image for a load balancer service."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getGraphImage', graphType, metric, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Service':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service import Network_Application_Delivery_Controller_LoadBalancer_Service
        return data

    def toggleStatus(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'toggleStatus', id=identifier)
        return data

    def getGroupReferences(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getGroupReferences', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference import Network_Application_Delivery_Controller_LoadBalancer_Service_Group_CrossReference
        return data

    def getGroups(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Service_Group']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getGroups', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group import Network_Application_Delivery_Controller_LoadBalancer_Service_Group
        return data

    def getHealthCheck(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Health_Check':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getHealthCheck', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Check import Network_Application_Delivery_Controller_LoadBalancer_Health_Check
        return data

    def getHealthChecks(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_Health_Check']:
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getHealthChecks', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Health_Check import Network_Application_Delivery_Controller_LoadBalancer_Health_Check
        return data

    def getIpAddress(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getIpAddress', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getServiceGroup(self, identifier: int) -> 'Network_Application_Delivery_Controller_LoadBalancer_Service_Group':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_Service', 'getServiceGroup', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_Service_Group import Network_Application_Delivery_Controller_LoadBalancer_Service_Group
        return data
