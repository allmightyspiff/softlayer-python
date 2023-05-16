# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template_Section_Reference(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template_Section_Reference'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Reference':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Reference import Reference
        return Reference(data)


    def getSection(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section':

        data = self.client.call(
            self.service,
            'getSection',
            mask=objectMask,
            filter=objectFilter
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


