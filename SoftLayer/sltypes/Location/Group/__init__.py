from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Location_Group(Entity):
    description: str
    id_: int
    locationGroupTypeId: int
    name: str
    securityLevelId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Group'

    def getAllObjects(self) -> list['Location_Group']:
        data = self.client.call('SoftLayer_Location_Group', 'getAllObjects')
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getObject(self, identifier: int) -> 'Location_Group':
        """Retrieve a SoftLayer_Location_Group record."""
        data = self.client.call('SoftLayer_Location_Group', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getLocationGroupType(self, identifier: int) -> 'Location_Group_Type':
        """"""
        data = self.client.call('SoftLayer_Location_Group', 'getLocationGroupType', id=identifier)
        from SoftLayer.sltypes.Location_Group_Type import Location_Group_Type
        return data

    def getLocations(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Location_Group', 'getLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data
