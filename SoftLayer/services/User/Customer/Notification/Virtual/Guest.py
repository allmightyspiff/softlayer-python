# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Notification_Virtual_Guest(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Notification_Virtual_Guest'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_User_Customer_Notification_Virtual_Guest,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_Notification_Virtual_Guest':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def createObjects(
        self,
        templateObjects: SoftLayer_User_Customer_Notification_Virtual_Guest,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObjects(
        self,
        templateObjects: SoftLayer_User_Customer_Notification_Virtual_Guest
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def findByGuestId(
        self,
        id: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'findByGuestId',
            id,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Notification_Virtual_Guest':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':
        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

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


