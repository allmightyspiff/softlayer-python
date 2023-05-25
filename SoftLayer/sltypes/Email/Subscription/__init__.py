from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Email_Subscription(Entity):
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Email_Subscription'

    def disable(self, identifier: int) -> bool:
        """Disable email subscription."""
        data = self.client.call('SoftLayer_Email_Subscription', 'disable', id=identifier)
        return data

    def enable(self, identifier: int) -> bool:
        """Enable email subscription."""
        data = self.client.call('SoftLayer_Email_Subscription', 'enable', id=identifier)
        return data

    def getAllObjects(self) -> list['Email_Subscription']:
        data = self.client.call('SoftLayer_Email_Subscription', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Email_Subscription':
        """Retrieve a SoftLayer_Email_Subscription record."""
        data = self.client.call('SoftLayer_Email_Subscription', 'getObject', id=identifier)
        return data

    def getEnabled(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Email_Subscription', 'getEnabled', id=identifier)
        return data
