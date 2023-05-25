from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Permission_Group(Entity):
    """The SoftLayer_User_Permission_Group data type contains local attributes to identify and describe the
permission groups that have been created within IMS.  These includes a name, description, and account id.
Permission groups are defined specifically for a single [[SoftLayer_Account]].   It also contains relational
attributes that indicate what SoftLayer_User_Permission_Action objects belong to a particular group, and what
SoftLayer_User_Permission_Role objects the group is linked."""
    accountId: int
    createDate: datetime
    description: str
    expirationDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Permission_Group'

    def addAction(self, identifier: int, action: 'User_Permission_Action') -> None:
        """Add a permission action to the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'addAction', action, id=identifier)
        return data

    def addBulkActions(self, identifier: int, actions: 'User_Permission_Action') -> None:
        """Adds a list of permission actions to the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'addBulkActions', actions, id=identifier)
        return data

    def addBulkResourceObjects(self, identifier: int, resourceObjects: 'Entity', resourceTypeKeyName: str) -> bool:
        """Links multiple account device objects of the same resource type to the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'addBulkResourceObjects', resourceObjects, resourceTypeKeyName, id=identifier)
        return data

    def addResourceObject(self, identifier: int, resourceObject: 'Entity', resourceTypeKeyName: str) -> bool:
        """Links a hardware, virtual guest, or dedicated host object on the"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'addResourceObject', resourceObject, resourceTypeKeyName, id=identifier)
        return data

    def createObject(self, templateObject: 'User_Permission_Group') -> 'User_Permission_Group':
        """Create a new customer permission group"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'createObject', templateObject)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a new customer permission group"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'User_Permission_Group') -> 'User_Permission_Group':
        """Edit an existing customer permission group"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'editObject', templateObject, id=identifier)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data

    def getObject(self, identifier: int) -> 'User_Permission_Group':
        """Retrieve a SoftLayer_User_Permission_Group record."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data

    def linkRole(self, identifier: int, role: 'User_Permission_Role') -> None:
        """Links a permission role to the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'linkRole', role, id=identifier)
        return data

    def removeAction(self, identifier: int, action: 'User_Permission_Action') -> None:
        """Remove a permission action from the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'removeAction', action, id=identifier)
        return data

    def removeBulkActions(self, identifier: int, actions: 'User_Permission_Action') -> None:
        """Remove a list of permission actions from the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'removeBulkActions', actions, id=identifier)
        return data

    def removeBulkResourceObjects(self, identifier: int, resourceObjects: 'Entity', resourceTypeKeyName: str) -> bool:
        """Unlinks multiple account device objects of the same resource type from the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'removeBulkResourceObjects', resourceObjects, resourceTypeKeyName, id=identifier)
        return data

    def removeResourceObject(self, identifier: int, resourceObject: 'Entity', resourceTypeKeyName: str) -> bool:
        """Unlinks a hardware, virtual guest, or dedicated host object on the"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'removeResourceObject', resourceObject, resourceTypeKeyName, id=identifier)
        return data

    def unlinkRole(self, identifier: int, role: 'User_Permission_Role') -> None:
        """Unlinks a permission role from the group."""
        data = self.client.call('SoftLayer_User_Permission_Group', 'unlinkRole', role, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActions(self, identifier: int) -> list['User_Permission_Action']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'getActions', id=identifier)
        from SoftLayer.sltypes.User_Permission_Action import User_Permission_Action
        return data

    def getRoles(self, identifier: int) -> list['User_Permission_Role']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'getRoles', id=identifier)
        from SoftLayer.sltypes.User_Permission_Role import User_Permission_Role
        return data

    def getType(self, identifier: int) -> 'User_Permission_Group_Type':
        """"""
        data = self.client.call('SoftLayer_User_Permission_Group', 'getType', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group_Type import User_Permission_Group_Type
        return data
