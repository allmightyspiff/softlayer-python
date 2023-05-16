# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Contact(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Contact'
        self.client = client

    def createComplianceReportRequestorContact(
        self,
        requestorTemplate: 'SoftLayer_Account_Contact',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Contact':

        data = self.client.call(
            self.service,
            'createComplianceReportRequestorContact',
            requestorTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


    def createObject(
        self,
        templateObject: 'SoftLayer_Account_Contact',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Contact':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


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
        templateObject: 'SoftLayer_Account_Contact',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getAllContactTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Contact_Type]':

        data = self.client.call(
            self.service,
            'getAllContactTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Contact.Type import Type
        return Type(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


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


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact.Type import Type
        return Type(data)


