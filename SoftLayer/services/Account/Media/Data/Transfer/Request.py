# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Media_Data_Transfer_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Media_Data_Transfer_Request'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Account_Media_Data_Transfer_Request
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllRequestStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Account_Media_Data_Transfer_Request_Status]':
        data = self.client.call(
            self.service,
            'getAllRequestStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Media.Data.Transfer.Request.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media_Data_Transfer_Request':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media.Data.Transfer.Request import Request
        return SL_Request(data)

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
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

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
    def getMedia(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media':
        data = self.client.call(
            self.service,
            'getMedia',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media import Media
        return SL_Media(data)

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
        return SL_Shipment(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Media_Data_Transfer_Request_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Media.Data.Transfer.Request.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Ticket(data)


