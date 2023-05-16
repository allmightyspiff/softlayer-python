# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Contact(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Contact'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createComplianceReportRequestorContact(
        self,
        requestorTemplate: SoftLayer_Account_Contact,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Contact':
        data = self.client.call(
            self.service,
            'createComplianceReportRequestorContact',
            requestorTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return SL_Contact(data)

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Account_Contact,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Contact':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return SL_Contact(data)

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
        templateObject: SoftLayer_Account_Contact
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return SL_Contact(data)

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
    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact_Type':
        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact.Type import Type
        return SL_Type(data)


