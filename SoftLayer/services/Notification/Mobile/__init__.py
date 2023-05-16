# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_Mobile(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_Mobile'
        self.client = client

    def createSubscriberForMobileDevice(
        self,
        keyName: str,
        resourceTableId: int,
        userRecordId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createSubscriberForMobileDevice',
            keyName,
            resourceTableId,
            userRecordId
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Mobile':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Mobile import Mobile
        return Mobile(data)


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Notification]':

        data = self.client.call(
            self.service,
            'getAllObjects',
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
    ) -> 'list[SoftLayer_Notification_Preference]':

        data = self.client.call(
            self.service,
            'getPreferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return Preference(data)


    def getRequiredPreferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Preference]':

        data = self.client.call(
            self.service,
            'getRequiredPreferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Preference import Preference
        return Preference(data)


