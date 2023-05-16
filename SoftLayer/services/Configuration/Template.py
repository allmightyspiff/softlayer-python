# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template'
        self.client = client

    def copyTemplate(
        self,
        templateObject: SoftLayer_Configuration_Template,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'copyTemplate',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


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
        templateObject: SoftLayer_Configuration_Template
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


    def updateDefaultValues(
        self,
        configurationValues: SoftLayer_Configuration_Template_Section_Definition_Value
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateDefaultValues',
            configurationValues
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


    def getConfigurationSections(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section]':

        data = self.client.call(
            self.service,
            'getConfigurationSections',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section import Section
        return Section(data)


    def getDefaultValues(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Definition_Value]':

        data = self.client.call(
            self.service,
            'getDefaultValues',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Value import Value
        return Value(data)


    def getDefinitions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Definition]':

        data = self.client.call(
            self.service,
            'getDefinitions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition import Definition
        return Definition(data)


    def getItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getLinkedSectionReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Reference':

        data = self.client.call(
            self.service,
            'getLinkedSectionReferences',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Reference import Reference
        return Reference(data)


    def getParent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getParent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


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


