from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Upgrade_Request(Entity):
    """The SoftLayer_Product_Upgrade_Request data type contains general information relating to a hardware, virtual
server, or service upgrade. It also relates a [[SoftLayer_Billing_Order]] to a [[SoftLayer_Ticket]]."""
    accountId: int
    createDate: datetime
    employeeId: int
    guestId: int
    hardwareId: int
    id_: int
    maintenanceStartTimeUtc: datetime
    modifyDate: datetime
    orderId: int
    orderTotal: float
    proratedTotal: float
    statusId: int
    ticketId: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Upgrade_Request'

    def approveChanges(self, identifier: int) -> bool:
        """Approves the upgrade request order that was revised by SoftLayer Sales"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'approveChanges', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Product_Upgrade_Request':
        """Retrieve a SoftLayer_Product_Upgrade_Request record."""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request import Product_Upgrade_Request
        return data

    def updateMaintenanceWindow(self, identifier: int, maintenanceStartTime: datetime, maintenanceWindowId: int) -> bool:
        """Updates the maintenance window"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'updateMaintenanceWindow', maintenanceStartTime, maintenanceWindowId, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getCompletedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getCompletedFlag', id=identifier)
        return data

    def getInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getOrder(self, identifier: int) -> 'Billing_Order':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getOrder', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getServer(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getServer', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getStatus(self, identifier: int) -> 'Product_Upgrade_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request_Status import Product_Upgrade_Request_Status
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getVirtualGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Product_Upgrade_Request', 'getVirtualGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
