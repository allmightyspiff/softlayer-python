# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_User_Subscriber_Preference(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_User_Subscriber_Preference'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Notification_User_Subscriber_Preference'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data


    def editObjects(
        self,
        templateObjects: 'SoftLayer_Notification_User_Subscriber_Preference'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber_Preference':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Preference import Preference
        return Preference(data)


    def getDefaultPreference(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Preference':

        data = self.client.call(
            self.service,
            'getDefaultPreference',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return Preference(data)


    def getNotificationUserSubscriber(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber':

        data = self.client.call(
            self.service,
            'getNotificationUserSubscriber',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


