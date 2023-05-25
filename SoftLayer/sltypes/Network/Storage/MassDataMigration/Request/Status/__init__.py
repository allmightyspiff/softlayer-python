from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_MassDataMigration_Request_Status(Entity):
    """The SoftLayer_Network_Storage_MassDataMigration_Request_Status data type contains general information
relating to the statuses to which a Mass Data Migration Request may be set."""
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_MassDataMigration_Request_Status'

    def getObject(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request_Status':
        """Retrieve a SoftLayer_Network_Storage_MassDataMigration_Request_Status record."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request_Status import Network_Storage_MassDataMigration_Request_Status
        return data
