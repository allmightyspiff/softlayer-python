from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Permission_Role(Entity):
    """The SoftLayer_User_Permission_Role data type contains local attributes to identify and describe the
permission roles that have been created within IMS.  These includes a name, description, and account id.
Permission groups are defined specifically for a single [[SoftLayer_Account]].   It also contains relational
attributes that indicate what SoftLayer_User_Permission_Group objects are linked to a particular role, and
the SoftLayer_User_Customer objects assigned to the role."""
    accountId: int
    createDate: datetime
    description: str
    id_: int
    modifyDate: datetime
    name: str
    newUserDefaultFlag: int
    systemFlag: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Permission_Role'

    def addUser(self, identifier: int, user: 'User_Customer') -> None:
        """Assign a user customer to the role."""
        data = self.client.call('SoftLayer_User_Permission_Role', 'addUser', user, id=identifier)
        return data

    def createObject(self, templateObject: 'User_Permission_Role') -> 'User_Permission_Role':
        """Create a new customer permission role"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a new customer permission role"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'User_Permission_Role') -> 'User_Permission_Role':
        """Edit an existing customer permission role"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'User_Permission_Role':
        """Retrieve a SoftLayer_User_Permission_Role record."""
        data = self.client.call('SoftLayer_User_Permission_Role', 'getObject', id=identifier)
        return data

    def linkGroup(self, identifier: int, group: 'User_Permission_Group') -> None:
        """Links a permission group to the role."""
        data = self.client.call('SoftLayer_User_Permission_Role', 'linkGroup', group, id=identifier)
        return data

    def removeUser(self, identifier: int, user: 'User_Customer') -> None:
        """Unassign a user customer from the role."""
        data = self.client.call('SoftLayer_User_Permission_Role', 'removeUser', user, id=identifier)
        return data

    def unlinkGroup(self, identifier: int, group: 'User_Permission_Group') -> None:
        """Unlinks a permission group to the role."""
        data = self.client.call('SoftLayer_User_Permission_Role', 'unlinkGroup', group, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActions(self, identifier: int) -> list['User_Permission_Action']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'getActions', id=identifier)
        from SoftLayer.sltypes.User_Permission_Action import User_Permission_Action
        return data

    def getGroups(self, identifier: int) -> list['User_Permission_Group']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'getGroups', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data

    def getUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Role', 'getUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
