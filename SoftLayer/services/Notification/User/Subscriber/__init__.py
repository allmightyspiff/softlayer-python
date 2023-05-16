# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_User_Subscriber(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_User_Subscriber'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Notification_User_Subscriber'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Notification_User_Subscriber',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getDeliveryMethods(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Delivery_Method]':

        data = self.client.call(
            self.service,
            'getDeliveryMethods',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Delivery.Method import Method
        return Method(data)


    def getNotification(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification':

        data = self.client.call(
            self.service,
            'getNotification',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification import Notification
        return Notification(data)


    def getPreferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber_Preference]':

        data = self.client.call(
            self.service,
            'getPreferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Preference import Preference
        return Preference(data)


    def getPreferencesDetails(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Preference]':

        data = self.client.call(
            self.service,
            'getPreferencesDetails',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return Preference(data)


    def getResourceRecord(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_User_Subscriber_Resource':

        data = self.client.call(
            self.service,
            'getResourceRecord',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.User.Subscriber.Resource import Resource
        return Resource(data)


    def getUserRecord(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUserRecord',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


