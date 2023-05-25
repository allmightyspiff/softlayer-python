from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Resource_Configuration(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Resource_Configuration'

    def setOsPasswordFromEncrypted(self, identifier: int, encryptedPassword: str) -> bool:
        """Set resource operating system password from an encrypted password"""
        data = self.client.call('SoftLayer_Resource_Configuration', 'setOsPasswordFromEncrypted', encryptedPassword, id=identifier)
        return data
