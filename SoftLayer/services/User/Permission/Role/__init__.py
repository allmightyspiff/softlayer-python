# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Permission_Role(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Permission_Role'
        self.client = client

    def addUser(
        self,
        user: 'SoftLayer_User_Customer',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addUser',
            user,
            id=identifier
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_User_Permission_Role',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Role':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_User_Permission_Role',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Role':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Role':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def linkGroup(
        self,
        group: 'SoftLayer_User_Permission_Group',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'linkGroup',
            group,
            id=identifier
        )
        
        return data


    def removeUser(
        self,
        user: 'SoftLayer_User_Customer',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeUser',
            user,
            id=identifier
        )
        
        return data


    def unlinkGroup(
        self,
        group: 'SoftLayer_User_Permission_Group',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unlinkGroup',
            group,
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getActions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Action]':

        data = self.client.call(
            self.service,
            'getActions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Action import Action
        return Action(data)


    def getGroups(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Group]':

        data = self.client.call(
            self.service,
            'getGroups',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def getUsers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getUsers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


