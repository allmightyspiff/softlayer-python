from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Media_Data_Transfer_Request(Entity):
    """The SoftLayer_Account_Media_Data_Transfer_Request data type contains information on a single Data Transfer
Service request. Creation of these requests is limited to SoftLayer customers through the SoftLayer Customer
Portal."""
    accountId: int
    createUserId: int
    endDate: datetime
    id_: int
    modifyUserId: int
    startDate: datetime
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Media_Data_Transfer_Request'

    def editObject(self, identifier: int, templateObject: 'Account_Media_Data_Transfer_Request') -> bool:
        """Edit a data transfer request."""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'editObject', templateObject, id=identifier)
        return data

    def getAllRequestStatuses(self) -> list['Account_Media_Data_Transfer_Request_Status']:
        """Retrieves a list of all the possible statuses to which a request may be set."""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getAllRequestStatuses')
        from SoftLayer.sltypes.Account_Media_Data_Transfer_Request_Status import Account_Media_Data_Transfer_Request_Status
        return data

    def getObject(self, identifier: int) -> 'Account_Media_Data_Transfer_Request':
        """Retrieve a SoftLayer_Account_Media_Data_Transfer_Request record."""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getActiveTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getMedia(self, identifier: int) -> 'Account_Media':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getMedia', id=identifier)
        from SoftLayer.sltypes.Account_Media import Account_Media
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getShipments(self, identifier: int) -> list['Account_Shipment']:
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getShipments', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data

    def getStatus(self, identifier: int) -> 'Account_Media_Data_Transfer_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Account_Media_Data_Transfer_Request_Status import Account_Media_Data_Transfer_Request_Status
        return data

    def getTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account_Media_Data_Transfer_Request', 'getTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data
