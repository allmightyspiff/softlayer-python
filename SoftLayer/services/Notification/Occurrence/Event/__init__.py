# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_Occurrence_Event(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_Occurrence_Event'
        self.client = client

    def acknowledgeNotification(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'acknowledgeNotification',
            id=identifier
        )
        
        return data


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getAttachedFile(
        self,
        attachmentId: int,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getAttachedFile',
            attachmentId,
            id=identifier
        )
        
        return data


    def getImpactedAccountCount(
        self,
        identifier: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getImpactedAccountCount',
            id=identifier
        )
        
        return data


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


    def getImpactedDevices(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Resource]':

        data = self.client.call(
            self.service,
            'getImpactedDevices',
            id=identifier,
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Resource import Resource
        return Resource(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getAcknowledgedFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAcknowledgedFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAttachments(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event_Attachment]':

        data = self.client.call(
            self.service,
            'getAttachments',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event.Attachment import Attachment
        return Attachment(data)


    def getFirstUpdate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Update':

        data = self.client.call(
            self.service,
            'getFirstUpdate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return Update(data)


    def getImpactedAccounts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Account]':

        data = self.client.call(
            self.service,
            'getImpactedAccounts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Account import Account
        return Account(data)


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


    def getImpactedUsers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_User]':

        data = self.client.call(
            self.service,
            'getImpactedUsers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.User import User
        return User(data)


    def getLastUpdate(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Update':

        data = self.client.call(
            self.service,
            'getLastUpdate',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return Update(data)


    def getNotificationOccurrenceEventType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event_Type':

        data = self.client.call(
            self.service,
            'getNotificationOccurrenceEventType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event.Type import Type
        return Type(data)


    def getStatusCode(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Status_Code':

        data = self.client.call(
            self.service,
            'getStatusCode',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Status.Code import Code
        return Code(data)


    def getUpdates(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Update]':

        data = self.client.call(
            self.service,
            'getUpdates',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return Update(data)


