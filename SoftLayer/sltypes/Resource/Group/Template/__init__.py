from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Resource_Group_Template(Entity):
    description: str
    id_: int
    keyName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Resource_Group_Template'

    def getAllObjects(self) -> list['Resource_Group_Template']:
        data = self.client.call('SoftLayer_Resource_Group_Template', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Resource_Group_Template':
        """Retrieve a SoftLayer_Resource_Group_Template record."""
        data = self.client.call('SoftLayer_Resource_Group_Template', 'getObject', id=identifier)
        return data

    def getChildren(self, identifier: int) -> list['Resource_Group_Template']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group_Template', 'getChildren', id=identifier)
        return data

    def getMembers(self, identifier: int) -> list['Resource_Group_Template_Member']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group_Template', 'getMembers', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Template_Member import Resource_Group_Template_Member
        return data
