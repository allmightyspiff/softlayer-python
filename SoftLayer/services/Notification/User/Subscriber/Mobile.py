# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_User_Subscriber_Mobile(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_User_Subscriber_Mobile'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def clearSnoozeTimer(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'clearSnoozeTimer',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber_Mobile':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Mobile import Mobile
        return SL_Mobile(data)

# This file was automatically generated with tools/generateTypes.py
    def setSnoozeTimer(
        self,
        start: int,
        end: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setSnoozeTimer',
            start,
            end
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Notification_User_Subscriber
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Notification_User_Subscriber
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDeliveryMethods(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Delivery_Method]':
        data = self.client.call(
            self.service,
            'getDeliveryMethods',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Delivery.Method import Method
        return SL_Method(data)

# This file was automatically generated with tools/generateTypes.py
    def getNotification(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification':
        data = self.client.call(
            self.service,
            'getNotification',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification import Notification
        return SL_Notification(data)

# This file was automatically generated with tools/generateTypes.py
    def getPreferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber_Preference]':
        data = self.client.call(
            self.service,
            'getPreferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Preference import Preference
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
    def getPreferencesDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Preference]':
        data = self.client.call(
            self.service,
            'getPreferencesDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return SL_Preference(data)

# This file was automatically generated with tools/generateTypes.py
    def getResourceRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber_Resource':
        data = self.client.call(
            self.service,
            'getResourceRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Resource import Resource
        return SL_Resource(data)

# This file was automatically generated with tools/generateTypes.py
    def getUserRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getUserRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


