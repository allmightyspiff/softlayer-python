# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template_Section(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template_Section'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section import Section
        return Section(data)


    def hasSubSections(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'hasSubSections',
            
        )
        
        return data


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


    def getDisallowedDeletionFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDisallowedDeletionFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLinkedTemplate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getLinkedTemplate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


    def getLinkedTemplateReference(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Reference':

        data = self.client.call(
            self.service,
            'getLinkedTemplateReference',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Reference import Reference
        return Reference(data)


    def getProfiles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Profile]':

        data = self.client.call(
            self.service,
            'getProfiles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Profile import Profile
        return Profile(data)


    def getSectionType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Type':

        data = self.client.call(
            self.service,
            'getSectionType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Type import Type
        return Type(data)


    def getSectionTypeName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSectionTypeName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSubSections(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section]':

        data = self.client.call(
            self.service,
            'getSubSections',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section import Section
        return Section(data)


    def getTemplate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getTemplate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


