# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_Occurrence_Event(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_Occurrence_Event'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def acknowledgeNotification(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'acknowledgeNotification',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedFile(
        self,
        attachmentId: int
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getAttachedFile',
            attachmentId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getImpactedAccountCount(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getImpactedAccountCount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getImpactedDeviceCount(
        self,
        
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getImpactedDeviceCount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getImpactedDevices(
        self,
        objectMask: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Resource]':
        data = self.client.call(
            self.service,
            'getImpactedDevices',
            mask=objectMask,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Resource import Resource
        return SL_Resource(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getAcknowledgedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getAcknowledgedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAttachments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event_Attachment]':
        data = self.client.call(
            self.service,
            'getAttachments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirstUpdate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Update':
        data = self.client.call(
            self.service,
            'getFirstUpdate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return SL_Update(data)

# This file was automatically generated with tools/generateTypes.py
    def getImpactedAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Account]':
        data = self.client.call(
            self.service,
            'getImpactedAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getImpactedResources(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Resource]':
        data = self.client.call(
            self.service,
            'getImpactedResources',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Resource import Resource
        return SL_Resource(data)

# This file was automatically generated with tools/generateTypes.py
    def getImpactedUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_User]':
        data = self.client.call(
            self.service,
            'getImpactedUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.User import User
        return SL_User(data)

# This file was automatically generated with tools/generateTypes.py
    def getLastUpdate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Update':
        data = self.client.call(
            self.service,
            'getLastUpdate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return SL_Update(data)

# This file was automatically generated with tools/generateTypes.py
    def getNotificationOccurrenceEventType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event_Type':
        data = self.client.call(
            self.service,
            'getNotificationOccurrenceEventType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatusCode(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Status_Code':
        data = self.client.call(
            self.service,
            'getStatusCode',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Status.Code import Code
        return SL_Code(data)

# This file was automatically generated with tools/generateTypes.py
    def getUpdates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Update]':
        data = self.client.call(
            self.service,
            'getUpdates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Update import Update
        return SL_Update(data)


