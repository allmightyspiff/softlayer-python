# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template_Section_Definition_Value(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template_Section_Definition_Value'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition_Value':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Value import Value
        return Value(data)


    def getDefinition(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition':

        data = self.client.call(
            self.service,
            'getDefinition',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition import Definition
        return Definition(data)


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


