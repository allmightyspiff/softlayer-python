from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Section_Type(Entity):
    """The SoftLayer_Configuration_Template_Section_Type data type contains information of a configuration section
type.   Configuration can contain sub-sections."""
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Section_Type'

    def getObject(self, identifier: int) -> 'Configuration_Template_Section_Type':
        """Retrieve a SoftLayer_Configuration_Template_Section_Type record."""
        data = self.client.call('SoftLayer_Configuration_Template_Section_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Type import Configuration_Template_Section_Type
        return data
