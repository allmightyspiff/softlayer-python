from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Reference(Entity):
    """The SoftLayer_Configuration_Template_Section_Reference data type contains information of a configuration
section and its associated configuration template."""
    createDate: datetime
    id_: int
    modifyDate: datetime
    sectionId: int
    templateId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Reference'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Reference':
        """Retrieve a SoftLayer_Configuration_Template_Section_Reference record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Reference', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Reference import Configuration_Template_Section_Reference
        return data

    def getSection(self, identifier: int) -> 'Configuration_Template_Section':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Reference', 'getSection', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data

    def getTemplate(self, identifier: int) -> 'Configuration_Template':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Reference', 'getTemplate', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data
