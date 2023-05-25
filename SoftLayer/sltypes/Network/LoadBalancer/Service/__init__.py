from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_LoadBalancer_Service(Entity):
    """The SoftLayer_Network_LoadBalancer_Service data type contains all the information relating to a specific
service (destination) on a particular load balancer.   Information retained on the object itself is the the
source and destination of the service, routing type, weight, and whether or not the service is currently
enabled."""
    connectionLimit: int
    createDate: datetime
    destinationIpAddress: str
    destinationPort: int
    enabled: bool
    healthCheck: str
    healthCheckURL: str
    healthResponse: str
    id_: int
    modifyDate: datetime
    name: str
    notes: str
    peakConnections: int
    sourcePort: int
    type_: str
    vipId: int
    weight: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_LoadBalancer_Service'

    def deleteObject(self, identifier: int) -> bool:
        """Delete this service, removing it from the load balancer."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'deleteObject', id=identifier)
        return data

    def getGraphImage(self, identifier: int, graphType: str, metric: str) -> str:
        """Get the connection or status graph image for a load balancer service."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'getGraphImage', graphType, metric, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_LoadBalancer_Service':
        """Retrieve a SoftLayer_Network_LoadBalancer_Service record."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Service import Network_LoadBalancer_Service
        return data

    def getStatus(self, identifier: int) -> list['Container_Network_LoadBalancer_StatusEntry']:
        """Returns various status entries for this service as an array of
SoftLayer_Container_Network_LoadBalancer_StatusEntry objects"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Container_Network_LoadBalancer_StatusEntry import Container_Network_LoadBalancer_StatusEntry
        return data

    def resetPeakConnections(self, identifier: int) -> bool:
        """Update the PeakConnections value on the service to zero."""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'resetPeakConnections', id=identifier)
        return data

    def getVip(self, identifier: int) -> 'Network_LoadBalancer_VirtualIpAddress':
        """"""
        data = self.client.call('SoftLayer_Network_LoadBalancer_Service', 'getVip', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_VirtualIpAddress import Network_LoadBalancer_VirtualIpAddress
        return data
