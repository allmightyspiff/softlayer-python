from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Resource_Group(Entity):
    createDate: datetime
    description: str
    id_: int
    keyName: str
    name: str
    rootResourceGroupId: int
    templateId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Resource_Group'

    def editObject(self, identifier: int, templateObject: 'Resource_Group') -> bool:
        data = self.client.call('SoftLayer_Resource_Group', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Resource_Group':
        """Retrieve a SoftLayer_Resource_Group record."""
        data = self.client.call('SoftLayer_Resource_Group', 'getObject', id=identifier)
        return data

    def getAncestorGroups(self, identifier: int) -> list['Resource_Group']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getAncestorGroups', id=identifier)
        return data

    def getAttributes(self, identifier: int) -> list['Resource_Group_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Attribute import Resource_Group_Attribute
        return data

    def getHardwareMembers(self, identifier: int) -> list['Resource_Group_Member']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getHardwareMembers', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Member import Resource_Group_Member
        return data

    def getMembers(self, identifier: int) -> list['Resource_Group_Member']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getMembers', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Member import Resource_Group_Member
        return data

    def getRootResourceGroup(self, identifier: int) -> 'Resource_Group':
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getRootResourceGroup', id=identifier)
        return data

    def getSubnetMembers(self, identifier: int) -> list['Resource_Group_Member']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getSubnetMembers', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Member import Resource_Group_Member
        return data

    def getTemplate(self, identifier: int) -> 'Resource_Group_Template':
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getTemplate', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Template import Resource_Group_Template
        return data

    def getVlanMembers(self, identifier: int) -> list['Resource_Group_Member']:
        """"""
        data = self.client.call('SoftLayer_Resource_Group', 'getVlanMembers', id=identifier)
        from SoftLayer.sltypes.Resource_Group_Member import Resource_Group_Member
        return data
