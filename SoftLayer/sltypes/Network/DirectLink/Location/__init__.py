from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_DirectLink_Location(Entity):
    """The SoftLayer_Network_DirectLink_Location presents a structure containing attributes of a Direct Link
location, and its related object SoftLayer location."""
    buildingColocationOwner: str
    id_: int
    isRedundantXcr: bool
    locationId: int
    marketGeography: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_DirectLink_Location'

    def getAllObjects(self) -> list['Network_DirectLink_Location']:
        """Get all existing Direct Link location."""
        data = self.client.call('SoftLayer_Network_DirectLink_Location', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_DirectLink_Location':
        """Retrieve a SoftLayer_Network_DirectLink_Location record."""
        data = self.client.call('SoftLayer_Network_DirectLink_Location', 'getObject', id=identifier)
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Network_DirectLink_Location', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getProvider(self, identifier: int) -> 'Network_DirectLink_Provider':
        """"""
        data = self.client.call('SoftLayer_Network_DirectLink_Location', 'getProvider', id=identifier)
        from SoftLayer.sltypes.Network_DirectLink_Provider import Network_DirectLink_Provider
        return data

    def getServiceType(self, identifier: int) -> 'Network_DirectLink_ServiceType':
        """"""
        data = self.client.call('SoftLayer_Network_DirectLink_Location', 'getServiceType', id=identifier)
        from SoftLayer.sltypes.Network_DirectLink_ServiceType import Network_DirectLink_ServiceType
        return data
