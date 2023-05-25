from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Shipment(Entity):
    """The SoftLayer_Account_Shipment data type contains information relating to a shipment. Basic information such
as addresses, the shipment courier, and any tracking information for as shipment is accessible with this data
type."""
    accountId: int
    courierId: int
    courierName: str
    createUserId: int
    destinationAddressId: int
    destinationDate: datetime
    id_: int
    modifyUserId: int
    note: str
    originationAddressId: int
    originationDate: datetime
    statusId: int
    typeId: int
    viaAddressId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Shipment'

    def editObject(self, identifier: int, templateObject: 'Account_Shipment') -> bool:
        """Edit a shipment record."""
        data = self.client.call('SoftLayer_Account_Shipment', 'editObject', templateObject, id=identifier)
        return data

    def getAllCouriers(self) -> list['Auxiliary_Shipping_Courier']:
        """Retrieve a list of available shipping couriers."""
        data = self.client.call('SoftLayer_Account_Shipment', 'getAllCouriers')
        from SoftLayer.sltypes.Auxiliary_Shipping_Courier import Auxiliary_Shipping_Courier
        return data

    def getAllCouriersByType(self, courierTypeKeyName: str) -> list['Auxiliary_Shipping_Courier']:
        """Retrieve a list of couriers for a given courier type"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getAllCouriersByType', courierTypeKeyName)
        from SoftLayer.sltypes.Auxiliary_Shipping_Courier import Auxiliary_Shipping_Courier
        return data

    def getAllShipmentStatuses(self) -> list['Account_Shipment_Status']:
        """Retrieve a list of shipment statuses."""
        data = self.client.call('SoftLayer_Account_Shipment', 'getAllShipmentStatuses')
        from SoftLayer.sltypes.Account_Shipment_Status import Account_Shipment_Status
        return data

    def getAllShipmentTypes(self) -> list['Account_Shipment_Type']:
        """Retrieve a list of shipment types."""
        data = self.client.call('SoftLayer_Account_Shipment', 'getAllShipmentTypes')
        from SoftLayer.sltypes.Account_Shipment_Type import Account_Shipment_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Shipment':
        """Retrieve a SoftLayer_Account_Shipment record."""
        data = self.client.call('SoftLayer_Account_Shipment', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getCourier(self, identifier: int) -> 'Auxiliary_Shipping_Courier':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getCourier', id=identifier)
        from SoftLayer.sltypes.Auxiliary_Shipping_Courier import Auxiliary_Shipping_Courier
        return data

    def getCreateEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getCreateEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getCurrency(self, identifier: int) -> 'Billing_Currency':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getCurrency', id=identifier)
        from SoftLayer.sltypes.Billing_Currency import Billing_Currency
        return data

    def getDestinationAddress(self, identifier: int) -> 'Account_Address':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getDestinationAddress', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getMasterTrackingData(self, identifier: int) -> 'Account_Shipment_Tracking_Data':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getMasterTrackingData', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Tracking_Data import Account_Shipment_Tracking_Data
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getOriginationAddress(self, identifier: int) -> 'Account_Address':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getOriginationAddress', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getShipmentItems(self, identifier: int) -> list['Account_Shipment_Item']:
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getShipmentItems', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Item import Account_Shipment_Item
        return data

    def getStatus(self, identifier: int) -> 'Account_Shipment_Status':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Status import Account_Shipment_Status
        return data

    def getTrackingData(self, identifier: int) -> list['Account_Shipment_Tracking_Data']:
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getTrackingData', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Tracking_Data import Account_Shipment_Tracking_Data
        return data

    def getType(self, identifier: int) -> 'Account_Shipment_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Shipment_Type import Account_Shipment_Type
        return data

    def getViaAddress(self, identifier: int) -> 'Account_Address':
        """"""
        data = self.client.call('SoftLayer_Account_Shipment', 'getViaAddress', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data
