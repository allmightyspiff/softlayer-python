from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Definition_Type(Entity):
    """SoftLayer_Configuration_Template_Section_Definition_Type further defines the value of a configuration
definition."""
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Definition_Type'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Definition_Type':
        """Retrieve a SoftLayer_Configuration_Template_Section_Definition_Type record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Definition_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Type import Configuration_Template_Section_Definition_Type
        return data
