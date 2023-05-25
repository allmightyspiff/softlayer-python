from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Definition(Entity):
    """Configuration definition gives you details of the value that you're setting.   If value type is defined as
"Resource Specific Values", you will have to make an additional API call to retrieve your system specific
values."""
    createDate: datetime
    description: str
    enumerationValues: str
    groupId: str
    id_: int
    maximumValue: str
    minimumValue: str
    modifyDate: datetime
    name: str
    path: str
    requireValueFlag: int
    sectionId: int
    shortName: str
    sort: int
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Definition'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Definition':
        """Retrieve a SoftLayer_Configuration_Template_Section_Definition record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition import Configuration_Template_Section_Definition
        return data

    def getAttributes(self, identifier: int) -> list['Configuration_Template_Section_Definition_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Attribute import Configuration_Template_Section_Definition_Attribute
        return data

    def getDefaultValue(self, identifier: int) -> 'Configuration_Template_Section_Definition_Value':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getDefaultValue', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Value import Configuration_Template_Section_Definition_Value
        return data

    def getGroup(self, identifier: int) -> 'Configuration_Template_Section_Definition_Group':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getGroup', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Group import Configuration_Template_Section_Definition_Group
        return data

    def getMonitoringDataFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getMonitoringDataFlag', id=identifier)
        return data

    def getSection(self, identifier: int) -> 'Configuration_Template_Section':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getSection', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data

    def getValueType(self, identifier: int) -> 'Configuration_Template_Section_Definition_Type':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition', 'getValueType', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Type import Configuration_Template_Section_Definition_Type
        return data
