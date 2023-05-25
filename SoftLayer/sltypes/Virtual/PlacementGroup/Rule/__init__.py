from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Virtual_PlacementGroup_Rule(Entity):
    """This data type presents the structure of a virtual guest placement group rule."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Virtual_PlacementGroup_Rule'

    def getAllObjects(self) -> list['Virtual_PlacementGroup_Rule']:
        """Get all placement group rules."""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup_Rule', 'getAllObjects')
        from SoftLayer.sltypes.Virtual_PlacementGroup_Rule import Virtual_PlacementGroup_Rule
        return data

    def getObject(self, identifier: int) -> 'Virtual_PlacementGroup_Rule':
        """Retrieve a SoftLayer_Virtual_PlacementGroup_Rule record."""
        data = self.client.call('SoftLayer_Virtual_PlacementGroup_Rule', 'getObject', id=identifier)
        from SoftLayer.sltypes.Virtual_PlacementGroup_Rule import Virtual_PlacementGroup_Rule
        return data
