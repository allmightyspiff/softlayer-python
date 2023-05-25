from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Definition_Group(Entity):
    """Configuration definition group gives you details of the definition and allows extra functionality."""
    createDate: datetime
    description: str
    id_: int
    name: str
    sortOrder: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Definition_Group'

    def getAllGroups(self) -> list['Configuration_Template_Section_Definition_Group']:
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Group', 'getAllGroups')
        return data

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Definition_Group':
        """Retrieve a SoftLayer_Configuration_Template_Section_Definition_Group record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Group', 'getObject', id=identifier)
        return data

    def getParent(self, identifier: int) -> 'Configuration_Template_Section_Definition_Group':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Group', 'getParent', id=identifier)
        return data
