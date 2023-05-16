# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Notification_Occurrence_User(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Notification_Occurrence_User'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def acknowledge(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'acknowledge',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_User(data)

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
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_User':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.User import User
        return SL_User(data)

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
    def getNotificationOccurrenceEvent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Notification_Occurrence_Event':
        data = self.client.call(
            self.service,
            'getNotificationOccurrenceEvent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return SL_Event(data)

# This file was automatically generated with tools/generateTypes.py
    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


