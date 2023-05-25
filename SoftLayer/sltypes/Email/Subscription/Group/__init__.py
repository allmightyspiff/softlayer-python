from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Email_Subscription_Group(Entity):
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Email_Subscription_Group'

    def getAllObjects(self) -> list['Email_Subscription_Group']:
        data = self.client.call('SoftLayer_Email_Subscription_Group', 'getAllObjects')
        from SoftLayer.sltypes.Email_Subscription_Group import Email_Subscription_Group
        return data

    def getObject(self, identifier: int) -> 'Email_Subscription_Group':
        """Retrieve a SoftLayer_Email_Subscription_Group record."""
        data = self.client.call('SoftLayer_Email_Subscription_Group', 'getObject', id=identifier)
        from SoftLayer.sltypes.Email_Subscription_Group import Email_Subscription_Group
        return data

    def getSubscriptions(self, identifier: int) -> list['Email_Subscription']:
        """"""
        data = self.client.call('SoftLayer_Email_Subscription_Group', 'getSubscriptions', id=identifier)
        from SoftLayer.sltypes.Email_Subscription import Email_Subscription
        return data
