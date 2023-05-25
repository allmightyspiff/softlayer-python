from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template_Type(Entity):
    """The SoftLayer_Configuration_Template_Type data type contains configuration template type information."""
    createDate: datetime
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template_Type'

    def getObject(self, identifier: int) -> 'Configuration_Template_Type':
        """Retrieve a SoftLayer_Configuration_Template_Type record."""
        data = self.client.call('SoftLayer_Configuration_Template_Type', 'getObject', id=identifier)
        return data
