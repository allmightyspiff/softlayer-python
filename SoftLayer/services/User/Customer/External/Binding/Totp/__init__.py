# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_External_Binding_Totp(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_External_Binding_Totp'
        self.client = client

    def activate(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activate',
            id=identifier
        )
        
        return data


    def deactivate(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deactivate',
            id=identifier
        )
        
        return data


    def generateSecretKey(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'generateSecretKey',
            
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_External_Binding_Totp':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.External.Binding.Totp import Totp
        return Totp(data)


    def disable(
        self,
        reason: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disable',
            reason,
            id=identifier
        )
        
        return data


    def enable(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enable',
            id=identifier
        )
        
        return data


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


    def updateNote(
        self,
        text: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateNote',
            text,
            id=identifier
        )
        
        return data


    def getUser(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getAttributes(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_External_Binding_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.External.Binding.Attribute import Attribute
        return Attribute(data)


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getNote(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNote',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_External_Binding_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Type import Type
        return Type(data)


    def getVendor(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_External_Binding_Vendor':

        data = self.client.call(
            self.service,
            'getVendor',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Vendor import Vendor
        return Vendor(data)


