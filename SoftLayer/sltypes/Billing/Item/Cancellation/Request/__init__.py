from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Item_Cancellation_Request(Entity):
    """SoftLayer_Billing_Item_Cancellation_Request data type is used to cancel service billing items."""
    accountId: int
    billingCancelReasonId: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    notes: str
    statusId: int
    ticketId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item_Cancellation_Request'

    def createObject(self, templateObject: 'Billing_Item_Cancellation_Request') -> 'Billing_Item_Cancellation_Request':
        """Creates a cancellation request."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'createObject', templateObject)
        return data

    def getAllCancellationRequests(self) -> list['Billing_Item_Cancellation_Request']:
        """Returns all service cancellation requests"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getAllCancellationRequests')
        return data

    def getCancellationCutoffDate(self, accountId: int, categoryCode: str) -> datetime:
        """Returns service cancellation cut off date."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getCancellationCutoffDate', accountId, categoryCode)
        return data

    def getObject(self, identifier: int) -> 'Billing_Item_Cancellation_Request':
        """Retrieve a SoftLayer_Billing_Item_Cancellation_Request record."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getObject', id=identifier)
        return data

    def removeCancellationItem(self, identifier: int, itemId: int) -> bool:
        """Removes a cancellation item"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'removeCancellationItem', itemId, id=identifier)
        return data

    def validateBillingItemForCancellation(self, billingItemId: int) -> bool:
        """Examined if a billing item can be canceled or not."""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'validateBillingItemForCancellation', billingItemId)
        return data

    def void(self, identifier: int, closeRelatedTicketFlag: bool) -> bool:
        """Voids a pending or approved cancellation request"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'void', closeRelatedTicketFlag, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getItems(self, identifier: int) -> list['Billing_Item_Cancellation_Request_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request_Item import Billing_Item_Cancellation_Request_Item
        return data

    def getStatus(self, identifier: int) -> 'Billing_Item_Cancellation_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request_Status import Billing_Item_Cancellation_Request_Status
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Cancellation_Request', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
