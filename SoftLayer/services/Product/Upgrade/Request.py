# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Upgrade_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Upgrade_Request'
        self.client = client

    def approveChanges(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'approveChanges',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Upgrade_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Upgrade.Request import Request
        return Request(data)


    def updateMaintenanceWindow(
        self,
        maintenanceStartTime: dateTime,
        maintenanceWindowId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateMaintenanceWindow',
            maintenanceStartTime,
            maintenanceWindowId
        )
        
        return data


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


    def getCompletedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCompletedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getOrder(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Order':

        data = self.client.call(
            self.service,
            'getOrder',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


    def getServer(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getServer',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Upgrade_Request_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Upgrade.Request.Status import Status
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
        return Customer(data)


    def getVirtualGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


