from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Security_Certificate_Request_ServerType(Entity):
    """Represents a server type that can be specified when ordering an SSL certificate."""
    description: str
    id_: int
    name: str
    value: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Security_Certificate_Request_ServerType'

    def getAllObjects(self) -> list['Security_Certificate_Request_ServerType']:
        """Returns all SSL certificate server types"""
        data = self.client.call('SoftLayer_Security_Certificate_Request_ServerType', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Security_Certificate_Request_ServerType':
        """Retrieve a SoftLayer_Security_Certificate_Request_ServerType record."""
        data = self.client.call('SoftLayer_Security_Certificate_Request_ServerType', 'getObject', id=identifier)
        return data
