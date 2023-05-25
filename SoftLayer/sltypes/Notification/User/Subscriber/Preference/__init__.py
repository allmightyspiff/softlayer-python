from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Notification_User_Subscriber_Preference(Entity):
    """Preferences are settings that can be modified to change the behavior of the subscription.  For example,
modify the limit preference to only receive notifications 10 times instead of 1 during a billing cycle.
NOTE: Some preferences have certain restrictions on values that can be set."""
    id_: int
    notificationPreferenceId: int
    notificationUserSubscriberId: int
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_User_Subscriber_Preference'

    def createObject(self, templateObject: 'Notification_User_Subscriber_Preference') -> bool:
        """Create a new notification preference for a subscriber."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Preference', 'createObject', templateObject)
        return data

    def editObjects(self, templateObjects: 'Notification_User_Subscriber_Preference') -> bool:
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Preference', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Notification_User_Subscriber_Preference':
        """Retrieve a SoftLayer_Notification_User_Subscriber_Preference record."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Preference', 'getObject', id=identifier)
        return data

    def getDefaultPreference(self, identifier: int) -> 'Notification_Preference':
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Preference', 'getDefaultPreference', id=identifier)
        from SoftLayer.sltypes.Notification_Preference import Notification_Preference
        return data

    def getNotificationUserSubscriber(self, identifier: int) -> 'Notification_User_Subscriber':
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Preference', 'getNotificationUserSubscriber', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
        return data
