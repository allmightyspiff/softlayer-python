from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_MassDataMigration_Request_KeyContact(Entity):
    """The SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact data type contains name, email, and phone
for key contact at customer location who will handle Mass Data Migration."""
    accountId: int
    createDate: datetime
    email: str
    id_: int
    modifyDate: datetime
    name: str
    phone: str
    requestId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact'

    def getObject(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request_KeyContact':
        """Retrieve a SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact record."""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getRequest(self, identifier: int) -> 'Network_Storage_MassDataMigration_Request':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact', 'getRequest', id=identifier)
        from SoftLayer.sltypes.Network_Storage_MassDataMigration_Request import Network_Storage_MassDataMigration_Request
        return data
