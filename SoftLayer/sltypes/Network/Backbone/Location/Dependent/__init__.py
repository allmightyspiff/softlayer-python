from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Backbone_Location_Dependent(Entity):
    dependentLocationId: int
    id_: int
    sourceLocationId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Backbone_Location_Dependent'

    def getAllObjects(self) -> list['Network_Backbone_Location_Dependent']:
        data = self.client.call('SoftLayer_Network_Backbone_Location_Dependent', 'getAllObjects')
        from SoftLayer.sltypes.Network_Backbone_Location_Dependent import Network_Backbone_Location_Dependent
        return data

    def getObject(self, identifier: int) -> 'Network_Backbone_Location_Dependent':
        """Retrieve a SoftLayer_Network_Backbone_Location_Dependent record."""
        data = self.client.call('SoftLayer_Network_Backbone_Location_Dependent', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Backbone_Location_Dependent import Network_Backbone_Location_Dependent
        return data

    def getSourceDependentsByName(self, locationName: str) -> 'Location':
        data = self.client.call('SoftLayer_Network_Backbone_Location_Dependent', 'getSourceDependentsByName', locationName)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDependentLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Backbone_Location_Dependent', 'getDependentLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getSourceLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_Backbone_Location_Dependent', 'getSourceLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data
