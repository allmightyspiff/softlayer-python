from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Business_Partner_Segment(Entity):
    """Contains business partner segment information"""
    description: str
    keyName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Business_Partner_Segment'

    def getObject(self, identifier: int) -> 'Business_Partner_Segment':
        """Retrieve a SoftLayer_Business_Partner_Segment record."""
        data = self.client.call('SoftLayer_Business_Partner_Segment', 'getObject', id=identifier)
        return data
