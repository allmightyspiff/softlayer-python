from SoftLayer.sltypes.Notification.User.Subscriber import Notification_User_Subscriber
from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
from SoftLayer import BaseClient

class Notification_User_Subscriber_Mobile(Notification_User_Subscriber):
    """A notification subscriber will have details pertaining to the subscriber's notification subscription.  You
can receive details such as preferences, details of the preferences, delivery methods and the delivery
methods for the subscriber.   NOTE: There are preferences and delivery methods that cannot be modified.
Also, there are some subscriptions that are required."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_User_Subscriber_Mobile'

    def clearSnoozeTimer(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Mobile', 'clearSnoozeTimer', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Notification_User_Subscriber_Mobile':
        """Retrieve a SoftLayer_Notification_User_Subscriber_Mobile record."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Mobile', 'getObject', id=identifier)
        return data

    def setSnoozeTimer(self, identifier: int, start: int, end: int) -> bool:
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Mobile', 'setSnoozeTimer', start, end, id=identifier)
        return data
