from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Backbone(Entity):
    """A SoftLayer_Network_Backbone represents a single backbone connection from SoftLayer to the public Internet,
from the Internet to the SoftLayer private network, or a link that connects the private networks between
SoftLayer's datacenters. The SoftLayer_Network_Backbone data type is a collection of data associated with one
of those connections."""
    capacity: int
    capacityUnits: str
    id_: int
    name: str
    networkComponentId: int
    type_: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Backbone'

    def getAllBackbones(self) -> list['Network_Backbone']:
        """Retrieve a list of all SoftLayer Backbones"""
        data = self.client.call('SoftLayer_Network_Backbone', 'getAllBackbones')
        return data

    def getBackbonesForLocationName(self, locationName: str) -> list['Network_Backbone']:
        """Retrieve a list of all SoftLayer Backbones for a location name"""
        data = self.client.call('SoftLayer_Network_Backbone', 'getBackbonesForLocationName', locationName)
        return data

    def getGraphImage(self, identifier: int) -> str:
        """[DEPRECATED] Retrieve a graph of a SoftLayer backbone's last 24 hours of activity."""
        data = self.client.call('SoftLayer_Network_Backbone', 'getGraphImage', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Backbone':
        """Retrieve a SoftLayer_Network_Backbone record."""
        data = self.client.call('SoftLayer_Network_Backbone', 'getObject', id=identifier)
        return data

    def getHealth(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Backbone', 'getHealth', id=identifier)
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Backbone', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getNetworkComponent(self, identifier: int) -> 'Network_Component':
        """"""
        data = self.client.call('SoftLayer_Network_Backbone', 'getNetworkComponent', id=identifier)
        from SoftLayer.sltypes.Network_Component import Network_Component
        return data
