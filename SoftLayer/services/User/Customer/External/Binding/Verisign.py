# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_External_Binding_Verisign(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_External_Binding_Verisign'
        self.client = client
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

# This file was automatically generated with tools/generateTypes.py
    def enable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'enable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getActivationCodeForMobileClient(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getActivationCodeForMobileClient',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_External_Binding_Verisign':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.External.Binding.Verisign import Verisign
        return SL_Verisign(data)

# This file was automatically generated with tools/generateTypes.py
    def unlock(
        self,
        securityCode: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'unlock',
            securityCode
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def validateCredentialId(
        self,
        userId: int,
        externalId: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'validateCredentialId',
            userId,
            externalId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getCredentialExpirationDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getCredentialExpirationDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCredentialLastUpdateDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getCredentialLastUpdateDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCredentialState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getCredentialState',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCredentialType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getCredentialType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Attribute(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Vendor(data)


