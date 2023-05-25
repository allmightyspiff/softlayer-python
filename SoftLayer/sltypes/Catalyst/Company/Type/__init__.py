from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Catalyst_Company_Type(Entity):
    description: str
    id_: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Catalyst_Company_Type'

    def getAllObjects(self) -> list['Catalyst_Company_Type']:
        """Get all catalyst company types"""
        data = self.client.call('SoftLayer_Catalyst_Company_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Catalyst_Company_Type':
        """Retrieve a SoftLayer_Catalyst_Company_Type record."""
        data = self.client.call('SoftLayer_Catalyst_Company_Type', 'getObject', id=identifier)
        return data
