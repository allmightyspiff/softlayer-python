from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Notification_User_Subscriber(Entity):
    """A notification subscriber will have details pertaining to the subscriber's notification subscription.  You
can receive details such as preferences, details of the preferences, delivery methods and the delivery
methods for the subscriber.   NOTE: There are preferences and delivery methods that cannot be modified.
Also, there are some subscriptions that are required."""
    active: int
    id_: int
    notificationId: int
    userRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Notification_User_Subscriber'

    def createObject(self, templateObject: 'Notification_User_Subscriber') -> bool:
        """Create a new notification subscriber."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'createObject', templateObject)
        return data

    def editObject(self, identifier: int, templateObject: 'Notification_User_Subscriber') -> bool:
        """Edit a notification subscriber active status"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Notification_User_Subscriber':
        """Retrieve a SoftLayer_Notification_User_Subscriber record."""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getObject', id=identifier)
        return data

    def getDeliveryMethods(self, identifier: int) -> list['Notification_Delivery_Method']:
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getDeliveryMethods', id=identifier)
        from SoftLayer.sltypes.Notification_Delivery_Method import Notification_Delivery_Method
        return data

    def getNotification(self, identifier: int) -> 'Notification':
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getNotification', id=identifier)
        from SoftLayer.sltypes.Notification import Notification
        return data

    def getPreferences(self, identifier: int) -> list['Notification_User_Subscriber_Preference']:
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getPreferences', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber_Preference import Notification_User_Subscriber_Preference
        return data

    def getPreferencesDetails(self, identifier: int) -> list['Notification_Preference']:
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getPreferencesDetails', id=identifier)
        from SoftLayer.sltypes.Notification_Preference import Notification_Preference
        return data

    def getResourceRecord(self, identifier: int) -> 'Notification_User_Subscriber_Resource':
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getResourceRecord', id=identifier)
        from SoftLayer.sltypes.Notification_User_Subscriber_Resource import Notification_User_Subscriber_Resource
        return data

    def getUserRecord(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Notification_User_Subscriber', 'getUserRecord', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
