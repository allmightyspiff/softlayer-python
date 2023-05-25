from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Business_Partner_Channel(Entity):
    """Contains business partner channel information"""
    description: str
    keyName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Business_Partner_Channel'

    def getObject(self, identifier: int) -> 'Business_Partner_Channel':
        """Retrieve a SoftLayer_Business_Partner_Channel record."""
        data = self.client.call('SoftLayer_Business_Partner_Channel', 'getObject', id=identifier)
        from SoftLayer.sltypes.Business_Partner_Channel import Business_Partner_Channel
        return data
