from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Notification(Entity):
    """Details provided for the notification are basic.  Details such as the related preferences, name and keyname
for the notification can be retrieved.  The keyname property for the notification can be used to refer to a
notification when integrating into the SoftLayer Notification system.  The name property can used more for
display purposes."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification'

    def getAllObjects(self) -> list['Notification']:
        """Retrieve all Notifications that can be subscribed to."""
        data = self.client.call('SoftLayer_Notification', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Notification':
        """Retrieve a SoftLayer_Notification record."""
        data = self.client.call('SoftLayer_Notification', 'getObject', id=identifier)
        return data

    def getPreferences(self, identifier: int) -> list['Notification_Preference']:
        """"""
        data = self.client.call('SoftLayer_Notification', 'getPreferences', id=identifier)
        from SoftLayer.sltypes.Notification_Preference import Notification_Preference
        return data

    def getRequiredPreferences(self, identifier: int) -> list['Notification_Preference']:
        """"""
        data = self.client.call('SoftLayer_Notification', 'getRequiredPreferences', id=identifier)
        from SoftLayer.sltypes.Notification_Preference import Notification_Preference
        return data
