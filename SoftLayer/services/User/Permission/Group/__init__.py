# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Permission_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Permission_Group'
        self.client = client

    def addAction(
        self,
        action: 'SoftLayer_User_Permission_Action',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addAction',
            action,
            id=identifier
        )
        
        return data


    def addBulkActions(
        self,
        actions: 'SoftLayer_User_Permission_Action',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addBulkActions',
            actions,
            id=identifier
        )
        
        return data


    def addBulkResourceObjects(
        self,
        resourceObjects: 'SoftLayer_Entity',
        resourceTypeKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkResourceObjects',
            resourceObjects,
            resourceTypeKeyName,
            id=identifier
        )
        
        return data


    def addResourceObject(
        self,
        resourceObject: 'SoftLayer_Entity',
        resourceTypeKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addResourceObject',
            resourceObject,
            resourceTypeKeyName,
            id=identifier
        )
        
        return data


    def createObject(
        self,
        templateObject: 'SoftLayer_User_Permission_Group',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Group':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


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
        templateObject: 'SoftLayer_User_Permission_Group',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Group':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Group':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def linkRole(
        self,
        role: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'linkRole',
            role,
            id=identifier
        )
        
        return data


    def removeAction(
        self,
        action: 'SoftLayer_User_Permission_Action',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeAction',
            action,
            id=identifier
        )
        
        return data


    def removeBulkActions(
        self,
        actions: 'SoftLayer_User_Permission_Action',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeBulkActions',
            actions,
            id=identifier
        )
        
        return data


    def removeBulkResourceObjects(
        self,
        resourceObjects: 'SoftLayer_Entity',
        resourceTypeKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkResourceObjects',
            resourceObjects,
            resourceTypeKeyName,
            id=identifier
        )
        
        return data


    def removeResourceObject(
        self,
        resourceObject: 'SoftLayer_Entity',
        resourceTypeKeyName: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeResourceObject',
            resourceObject,
            resourceTypeKeyName,
            id=identifier
        )
        
        return data


    def unlinkRole(
        self,
        role: 'SoftLayer_User_Permission_Role',
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unlinkRole',
            role,
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


    def getRoles(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Role]':

        data = self.client.call(
            self.service,
            'getRoles',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Group_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Group.Type import Type
        return Type(data)


