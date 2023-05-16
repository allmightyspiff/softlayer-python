# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Item_Cancellation_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Item_Cancellation_Request'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Billing_Item_Cancellation_Request',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return Request(data)


    def getAllCancellationRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Request]':

        data = self.client.call(
            self.service,
            'getAllCancellationRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return Request(data)


    def getCancellationCutoffDate(
        self,
        accountId: int,
        categoryCode: str
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getCancellationCutoffDate',
            accountId,
            categoryCode
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return Request(data)


    def removeCancellationItem(
        self,
        itemId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeCancellationItem',
            itemId,
            id=identifier
        )
        
        return data


    def validateBillingItemForCancellation(
        self,
        billingItemId: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateBillingItemForCancellation',
            billingItemId
        )
        
        return data


    def void(
        self,
        closeRelatedTicketFlag: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'void',
            closeRelatedTicketFlag,
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getItems(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Request_Item]':

        data = self.client.call(
            self.service,
            'getItems',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request.Item import Item
        return Item(data)


    def getStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request.Status import Status
        return Status(data)


    def getTicket(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':

        data = self.client.call(
            self.service,
            'getTicket',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


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


