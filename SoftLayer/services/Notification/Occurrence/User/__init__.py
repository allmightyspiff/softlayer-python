# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_Occurrence_User(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_Occurrence_User'
        self.client = client

    def acknowledge(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'acknowledge',
            id=identifier
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_User]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.User import User
        return User(data)


    def getImpactedDeviceCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getImpactedDeviceCount',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_User':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.User import User
        return User(data)


    def getImpactedResources(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Resource]':

        data = self.client.call(
            self.service,
            'getImpactedResources',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Resource import Resource
        return Resource(data)


    def getNotificationOccurrenceEvent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event':

        data = self.client.call(
            self.service,
            'getNotificationOccurrenceEvent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getUser(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


