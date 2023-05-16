# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template_Section(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template_Section'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section import Section
        return Section(data)


    def hasSubSections(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'hasSubSections',
            id=identifier
        )
        
        return data


    def getDefinitions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Definition]':

        data = self.client.call(
            self.service,
            'getDefinitions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition import Definition
        return Definition(data)


    def getDisallowedDeletionFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDisallowedDeletionFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLinkedTemplate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getLinkedTemplate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


    def getLinkedTemplateReference(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Reference':

        data = self.client.call(
            self.service,
            'getLinkedTemplateReference',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Reference import Reference
        return Reference(data)


    def getProfiles(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Profile]':

        data = self.client.call(
            self.service,
            'getProfiles',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Profile import Profile
        return Profile(data)


    def getSectionType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Type':

        data = self.client.call(
            self.service,
            'getSectionType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Type import Type
        return Type(data)


    def getSectionTypeName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSectionTypeName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSubSections(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section]':

        data = self.client.call(
            self.service,
            'getSubSections',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section import Section
        return Section(data)


    def getTemplate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template':

        data = self.client.call(
            self.service,
            'getTemplate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


