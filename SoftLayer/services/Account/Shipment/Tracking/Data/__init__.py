# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Shipment_Tracking_Data(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Shipment_Tracking_Data'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Account_Shipment_Tracking_Data',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Shipment_Tracking_Data':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Shipment.Tracking.Data import Data
        return Data(data)


    def createObjects(
        self,
        templateObjects: 'SoftLayer_Account_Shipment_Tracking_Data',
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Shipment_Tracking_Data]':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Shipment.Tracking.Data import Data
        return Data(data)


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
        templateObject: 'SoftLayer_Account_Shipment_Tracking_Data',
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
    ) -> 'SoftLayer_Account_Shipment_Tracking_Data':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Tracking.Data import Data
        return Data(data)


    def getCreateEmployee(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getCreateEmployee',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getCreateUser(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCreateUser',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getModifyEmployee(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getModifyEmployee',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getModifyUser(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getModifyUser',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getShipment(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment':

        data = self.client.call(
            self.service,
            'getShipment',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment import Shipment
        return Shipment(data)


