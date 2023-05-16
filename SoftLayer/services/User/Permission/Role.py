# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Permission_Role(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Permission_Role'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addUser(
        self,
        user: SoftLayer_User_Customer
    ) -> 'void':
        data = self.client.call(
            self.service,
            'addUser',
            user
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_User_Permission_Role,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Role':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return SL_Role(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_User_Permission_Role,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Role':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return SL_Role(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Role':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return SL_Role(data)

# This file was automatically generated with tools/generateTypes.py
    def linkGroup(
        self,
        group: SoftLayer_User_Permission_Group
    ) -> 'void':
        data = self.client.call(
            self.service,
            'linkGroup',
            group
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeUser(
        self,
        user: SoftLayer_User_Customer
    ) -> 'void':
        data = self.client.call(
            self.service,
            'removeUser',
            user
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def unlinkGroup(
        self,
        group: SoftLayer_User_Permission_Group
    ) -> 'void':
        data = self.client.call(
            self.service,
            'unlinkGroup',
            group
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getActions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Action]':
        data = self.client.call(
            self.service,
            'getActions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Action import Action
        return SL_Action(data)

# This file was automatically generated with tools/generateTypes.py
    def getGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Group]':
        data = self.client.call(
            self.service,
            'getGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':
        data = self.client.call(
            self.service,
            'getUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


