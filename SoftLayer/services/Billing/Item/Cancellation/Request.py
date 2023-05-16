# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Item_Cancellation_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Item_Cancellation_Request'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Billing_Item_Cancellation_Request,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def removeCancellationItem(
        self,
        itemId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeCancellationItem',
            itemId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def void(
        self,
        closeRelatedTicketFlag: boolean
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'void',
            closeRelatedTicketFlag
        )
        
        return data

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
    def getItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Request_Item]':
        data = self.client.call(
            self.service,
            'getItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)


