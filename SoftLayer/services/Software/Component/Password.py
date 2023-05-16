# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Software_Component_Password(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Software_Component_Password'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Software_Component_Password,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Software_Component_Password':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


    def createObjects(
        self,
        templateObjects: SoftLayer_Software_Component_Password
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects
        )
        
        return data


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def deleteObjects(
        self,
        templateObjects: SoftLayer_Software_Component_Password
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Software_Component_Password
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: SoftLayer_Software_Component_Password
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_Password':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


    def getSoftware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getSoftware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getSshKeys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':

        data = self.client.call(
            self.service,
            'getSshKeys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return Key(data)


