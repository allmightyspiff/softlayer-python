# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_MobileDevice(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_MobileDevice'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_User_Customer_MobileDevice,
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
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_User_Customer_MobileDevice
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice import MobileDevice
        return MobileDevice(data)


    def getAvailablePushNotificationSubscriptions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification]':

        data = self.client.call(
            self.service,
            'getAvailablePushNotificationSubscriptions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification import Notification
        return Notification(data)


    def getCustomer(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCustomer',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getOperatingSystem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice_OperatingSystem':

        data = self.client.call(
            self.service,
            'getOperatingSystem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getPushNotificationSubscriptions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_User_Subscriber]':

        data = self.client.call(
            self.service,
            'getPushNotificationSubscriptions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.User.Subscriber import Subscriber
        return Subscriber(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_MobileDevice_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.MobileDevice.Type import Type
        return Type(data)


