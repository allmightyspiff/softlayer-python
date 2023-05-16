# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_User_Subscriber_Preference(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_User_Subscriber_Preference'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Notification_User_Subscriber_Preference
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObjects(
        self,
        templateObjects: SoftLayer_Notification_User_Subscriber_Preference
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber_Preference':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Preference import Preference
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
    def getDefaultPreference(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Preference':
        data = self.client.call(
            self.service,
            'getDefaultPreference',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
    def getNotificationUserSubscriber(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber':
        data = self.client.call(
            self.service,
            'getNotificationUserSubscriber',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return SL_Subscriber(data)


