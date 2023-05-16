# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Notification_Hardware(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Notification_Hardware'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_User_Customer_Notification_Hardware',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer_Notification_Hardware':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_User_Customer_Notification_Hardware',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Hardware]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def deleteObjects(
        self,
        templateObjects: 'SoftLayer_User_Customer_Notification_Hardware'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def findByHardwareId(
        self,
        hardwareId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Customer_Notification_Hardware]':

        data = self.client.call(
            self.service,
            'findByHardwareId',
            hardwareId,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Notification_Hardware':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Notification.Hardware import Hardware
        return Hardware(data)


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


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


