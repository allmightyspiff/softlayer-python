# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Shipment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Shipment'
        self.client = client

    def editObject(
        self,
        templateObject: SoftLayer_Account_Shipment
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getAllCouriers(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Auxiliary_Shipping_Courier]':

        data = self.client.call(
            self.service,
            'getAllCouriers',
            mask=objectMask
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier import Courier
        return Courier(data)


    def getAllCouriersByType(
        self,
        courierTypeKeyName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Auxiliary_Shipping_Courier]':

        data = self.client.call(
            self.service,
            'getAllCouriersByType',
            courierTypeKeyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier import Courier
        return Courier(data)


    def getAllShipmentStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Shipment_Status]':

        data = self.client.call(
            self.service,
            'getAllShipmentStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Shipment.Status import Status
        return Status(data)


    def getAllShipmentTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Shipment_Type]':

        data = self.client.call(
            self.service,
            'getAllShipmentTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Shipment.Type import Type
        return Type(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment import Shipment
        return Shipment(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getCourier(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Shipping_Courier':

        data = self.client.call(
            self.service,
            'getCourier',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Shipping.Courier import Courier
        return Courier(data)


    def getCreateEmployee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getCreateEmployee',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getCreateUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCreateUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getCurrency(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Currency':

        data = self.client.call(
            self.service,
            'getCurrency',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Currency import Currency
        return Currency(data)


    def getDestinationAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getDestinationAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getMasterTrackingData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment_Tracking_Data':

        data = self.client.call(
            self.service,
            'getMasterTrackingData',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Tracking.Data import Data
        return Data(data)


    def getModifyEmployee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Employee':

        data = self.client.call(
            self.service,
            'getModifyEmployee',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getModifyUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getModifyUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getOriginationAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getOriginationAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getShipmentItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Shipment_Item]':

        data = self.client.call(
            self.service,
            'getShipmentItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Shipment.Item import Item
        return Item(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Status import Status
        return Status(data)


    def getTrackingData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Shipment_Tracking_Data]':

        data = self.client.call(
            self.service,
            'getTrackingData',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Shipment.Tracking.Data import Data
        return Data(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Shipment_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Shipment.Type import Type
        return Type(data)


    def getViaAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getViaAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


