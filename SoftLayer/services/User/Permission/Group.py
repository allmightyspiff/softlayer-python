# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Permission_Group(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Permission_Group'
        self.client = client

    def addAction(
        self,
        action: SoftLayer_User_Permission_Action
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addAction',
            action
        )
        
        return data


    def addBulkActions(
        self,
        actions: SoftLayer_User_Permission_Action
    ) -> 'void':

        data = self.client.call(
            self.service,
            'addBulkActions',
            actions
        )
        
        return data


    def addBulkResourceObjects(
        self,
        resourceObjects: SoftLayer_Entity,
        resourceTypeKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addBulkResourceObjects',
            resourceObjects,
            resourceTypeKeyName
        )
        
        return data


    def addResourceObject(
        self,
        resourceObject: SoftLayer_Entity,
        resourceTypeKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addResourceObject',
            resourceObject,
            resourceTypeKeyName
        )
        
        return data


    def createObject(
        self,
        templateObject: SoftLayer_User_Permission_Group,
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
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_User_Permission_Group,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Permission_Group':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Group':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def linkRole(
        self,
        role: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'linkRole',
            role
        )
        
        return data


    def removeAction(
        self,
        action: SoftLayer_User_Permission_Action
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeAction',
            action
        )
        
        return data


    def removeBulkActions(
        self,
        actions: SoftLayer_User_Permission_Action
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeBulkActions',
            actions
        )
        
        return data


    def removeBulkResourceObjects(
        self,
        resourceObjects: SoftLayer_Entity,
        resourceTypeKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeBulkResourceObjects',
            resourceObjects,
            resourceTypeKeyName
        )
        
        return data


    def removeResourceObject(
        self,
        resourceObject: SoftLayer_Entity,
        resourceTypeKeyName: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeResourceObject',
            resourceObject,
            resourceTypeKeyName
        )
        
        return data


    def unlinkRole(
        self,
        role: SoftLayer_User_Permission_Role
    ) -> 'void':

        data = self.client.call(
            self.service,
            'unlinkRole',
            role
        )
        
        return data


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
        return Account(data)


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
        return Action(data)


    def getRoles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Role]':

        data = self.client.call(
            self.service,
            'getRoles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Permission_Group_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Permission.Group.Type import Type
        return Type(data)


