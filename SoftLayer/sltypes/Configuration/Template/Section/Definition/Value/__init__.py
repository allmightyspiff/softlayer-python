from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Definition_Value(Entity):
    """SoftLayer_Configuration_Section_Value is used to set the value for a configuration definition"""
    createDate: datetime
    definitionId: int
    modifyDate: datetime
    templateId: int
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Definition_Value'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Definition_Value':
        """Retrieve a SoftLayer_Configuration_Template_Section_Definition_Value record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Value', 'getObject', id=identifier)
        return data

    def getDefinition(self, identifier: int) -> 'Configuration_Template_Section_Definition':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Value', 'getDefinition', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition import Configuration_Template_Section_Definition
        return data

    def getTemplate(self, identifier: int) -> 'Configuration_Template':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Value', 'getTemplate', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data
