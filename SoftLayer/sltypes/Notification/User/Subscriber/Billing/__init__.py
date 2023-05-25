from SoftLayer.sltypes.Notification.User.Subscriber import Notification_User_Subscriber
from SoftLayer.sltypes.Notification_User_Subscriber import Notification_User_Subscriber
from SoftLayer import BaseClient

class Notification_User_Subscriber_Billing(Notification_User_Subscriber):
    """A notification subscriber will have details pertaining to the subscriber's notification subscription.  You
can receive details such as preferences, details of the preferences, delivery methods and the delivery
methods for the subscriber.   NOTE: There are preferences and delivery methods that cannot be modified.
Also, there are some subscriptions that are required."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_User_Subscriber_Billing'

    def getObject(self, identifier: int) -> 'Notification_User_Subscriber_Billing':
        """Retrieve a SoftLayer_Notification_User_Subscriber_Billing record."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber_Billing', 'getObject', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber_Billing import Notification_User_Subscriber_Billing
        return data
