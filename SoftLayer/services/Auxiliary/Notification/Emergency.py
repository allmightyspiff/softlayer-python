# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Auxiliary_Notification_Emergency(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Auxiliary_Notification_Emergency'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Auxiliary_Notification_Emergency]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Notification.Emergency import Emergency
        return SL_Emergency(data)

# This file was automatically generated with tools/generateTypes.py
    def getCurrentNotifications(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Auxiliary_Notification_Emergency]':
        data = self.client.call(
            self.service,
            'getCurrentNotifications',
            mask=objectMask
        )
        from SoftLayer.datatypes.Auxiliary.Notification.Emergency import Emergency
        return SL_Emergency(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Notification_Emergency':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Notification.Emergency import Emergency
        return SL_Emergency(data)

# This file was automatically generated with tools/generateTypes.py
    def getSignature(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Notification_Emergency_Signature':
        data = self.client.call(
            self.service,
            'getSignature',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Notification.Emergency.Signature import Signature
        return SL_Signature(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Notification_Emergency_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Notification.Emergency.Status import Status
        return SL_Status(data)


