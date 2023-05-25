from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Profile(Entity):
    """Some configuration templates let you create a unique configuration profiles.   For example, you can create
multiple configuration profiles to monitor multiple hard drives with "CPU/Memory/Disk Monitoring Agent".
SoftLayer_Configuration_Template_Section_Profile help you keep track of custom configuration profiles."""
    agentId: int
    createDate: datetime
    id_: int
    name: str
    sectionId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Profile'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Profile':
        """Retrieve a SoftLayer_Configuration_Template_Section_Profile record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Profile', 'getObject', id=identifier)
        return data

    def getConfigurationSection(self, identifier: int) -> 'Configuration_Template_Section':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Profile', 'getConfigurationSection', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data
