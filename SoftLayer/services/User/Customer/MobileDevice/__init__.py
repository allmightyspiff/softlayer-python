# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_MobileDevice(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_MobileDevice'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_User_Customer_MobileDevice',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice import MobileDevice
        return MobileDevice(data)


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_User_Customer_MobileDevice',
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
    ) -> 'SoftLayer_User_Customer_MobileDevice':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice import MobileDevice
        return MobileDevice(data)


    def getAvailablePushNotificationSubscriptions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification]':

        data = self.client.call(
            self.service,
            'getAvailablePushNotificationSubscriptions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification import Notification
        return Notification(data)


    def getCustomer(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCustomer',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getOperatingSystem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice_OperatingSystem':

        data = self.client.call(
            self.service,
            'getOperatingSystem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getPushNotificationSubscriptions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getPushNotificationSubscriptions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.Type import Type
        return Type(data)


