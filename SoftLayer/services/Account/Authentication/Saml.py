# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Authentication_Saml(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Authentication_Saml'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Account_Authentication_Saml,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Authentication_Saml':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Authentication.Saml import Saml
        return SL_Saml(data)

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
        templateObject: SoftLayer_Account_Authentication_Saml
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getMetadata(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getMetadata',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Authentication_Saml':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Authentication.Saml import Saml
        return SL_Saml(data)

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
    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Authentication_Attribute]':
        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Authentication.Attribute import Attribute
        return SL_Attribute(data)


