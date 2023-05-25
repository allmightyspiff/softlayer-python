from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section(Entity):
    """The SoftLayer_Configuration_Template_Section data type contains information of a configuration section.
Configuration can contain sub-sections."""
    createDate: datetime
    description: str
    id_: int
    linkedTemplateId: str
    modifyDate: datetime
    name: str
    parentId: int
    sort: int
    templateId: str
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section':
        """Retrieve a SoftLayer_Configuration_Template_Section record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data

    def hasSubSections(self, identifier: int) -> bool:
        """Check if object has sub-sections"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'hasSubSections', id=identifier)
        return data

    def getDefinitions(self, identifier: int) -> list['Configuration_Template_Section_Definition']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getDefinitions', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition import Configuration_Template_Section_Definition
        return data

    def getDisallowedDeletionFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getDisallowedDeletionFlag', id=identifier)
        return data

    def getLinkedTemplate(self, identifier: int) -> 'Configuration_Template':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getLinkedTemplate', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def getLinkedTemplateReference(self, identifier: int) -> 'Configuration_Template_Section_Reference':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getLinkedTemplateReference', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Reference import Configuration_Template_Section_Reference
        return data

    def getProfiles(self, identifier: int) -> list['Configuration_Template_Section_Profile']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getProfiles', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Profile import Configuration_Template_Section_Profile
        return data

    def getSectionType(self, identifier: int) -> 'Configuration_Template_Section_Type':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getSectionType', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Type import Configuration_Template_Section_Type
        return data

    def getSectionTypeName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getSectionTypeName', id=identifier)
        return data

    def getSubSections(self, identifier: int) -> list['Configuration_Template_Section']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getSubSections', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data

    def getTemplate(self, identifier: int) -> 'Configuration_Template':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section', 'getTemplate', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data
