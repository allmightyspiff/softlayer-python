# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Template_Section_Definition(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Template_Section_Definition'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition import Definition
        return Definition(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template_Section_Definition_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Attribute import Attribute
        return Attribute(data)


    def getDefaultValue(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition_Value':

        data = self.client.call(
            self.service,
            'getDefaultValue',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Value import Value
        return Value(data)


    def getGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition_Group':

        data = self.client.call(
            self.service,
            'getGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Group import Group
        return Group(data)


    def getMonitoringDataFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMonitoringDataFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getValueType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Template_Section_Definition_Type':

        data = self.client.call(
            self.service,
            'getValueType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Template.Section.Definition.Type import Type
        return Type(data)


