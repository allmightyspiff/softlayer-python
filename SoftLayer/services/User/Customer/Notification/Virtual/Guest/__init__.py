# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Notification_Virtual_Guest(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Notification_Virtual_Guest'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_User_Customer_Notification_Virtual_Guest',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_Notification_Virtual_Guest':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return Guest(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_User_Customer_Notification_Virtual_Guest',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return Guest(data)


    def deleteObjects(
        self,
        templateObjects: 'SoftLayer_User_Customer_Notification_Virtual_Guest'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


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
        return Guest(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Notification_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Notification.Virtual.Guest import Guest
        return Guest(data)


    def getGuest(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getGuest',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


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


