from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Security_Certificate_Request_Status(Entity):
    """Represents the status of an SSL certificate request."""
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Security_Certificate_Request_Status'

    def getObject(self, identifier: int) -> 'Security_Certificate_Request_Status':
        """Retrieve a SoftLayer_Security_Certificate_Request_Status record."""
        data = self.client.call('SoftLayer_Security_Certificate_Request_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Security_Certificate_Request_Status import Security_Certificate_Request_Status
        return data

    def getSslRequestStatuses(self) -> list['Security_Certificate_Request_Status']:
        """Returns all SSL certificate request status objects"""
        data = self.client.call('SoftLayer_Security_Certificate_Request_Status', 'getSslRequestStatuses')
        from SoftLayer.sltypes.Security_Certificate_Request_Status import Security_Certificate_Request_Status
        return data
