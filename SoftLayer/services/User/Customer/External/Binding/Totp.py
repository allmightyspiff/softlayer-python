# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_External_Binding_Totp(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_External_Binding_Totp'
        self.client = client

    def activate(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'activate',
            
        )
        
        return data


    def deactivate(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deactivate',
            
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
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_External_Binding_Totp':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.External.Binding.Totp import Totp
        return Totp(data)


    def disable(
        self,
        reason: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disable',
            reason
        )
        
        return data


    def enable(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enable',
            
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


    def updateNote(
        self,
        text: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateNote',
            text
        )
        
        return data


    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_External_Binding_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.External.Binding.Attribute import Attribute
        return Attribute(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getNote(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getNote',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_External_Binding_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Type import Type
        return Type(data)


    def getVendor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_External_Binding_Vendor':

        data = self.client.call(
            self.service,
            'getVendor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.External.Binding.Vendor import Vendor
        return Vendor(data)


