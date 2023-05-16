# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Shipment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Shipment'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Courier(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Courier(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Shipment(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Courier(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Employee(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Currency(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Address(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Employee(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Address(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Address(data)


