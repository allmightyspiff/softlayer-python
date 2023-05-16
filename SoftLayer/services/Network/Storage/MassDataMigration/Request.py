# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_MassDataMigration_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_MassDataMigration_Request'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_Request]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request import Request
        return Request(data)


    def getAllRequestStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_Request_Status]':

        data = self.client.call(
            self.service,
            'getAllRequestStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request.Status import Status
        return Status(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_MassDataMigration_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request import Request
        return Request(data)


    def getPendingRequests(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_Request]':

        data = self.client.call(
            self.service,
            'getPendingRequests',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request import Request
        return Request(data)


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


    def getActiveTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getActiveTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


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


    def getDeviceConfiguration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_MassDataMigration_Request_DeviceConfiguration':

        data = self.client.call(
            self.service,
            'getDeviceConfiguration',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request.DeviceConfiguration import DeviceConfiguration
        return DeviceConfiguration(data)


    def getDeviceModel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDeviceModel',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getKeyContacts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact]':

        data = self.client.call(
            self.service,
            'getKeyContacts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request.KeyContact import KeyContact
        return KeyContact(data)


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


    def getShipments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Shipment]':

        data = self.client.call(
            self.service,
            'getShipments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Shipment import Shipment
        return Shipment(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_MassDataMigration_Request_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.MassDataMigration.Request.Status import Status
        return Status(data)


    def getTicket(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':

        data = self.client.call(
            self.service,
            'getTicket',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


