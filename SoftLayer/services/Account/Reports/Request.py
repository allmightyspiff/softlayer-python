# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Reports_Request(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Reports_Request'
        self.client = client

    def createRequest(
        self,
        recipientContact: SoftLayer_Account_Contact,
        reason: str,
        reportType: str,
        requestorContact: SoftLayer_Account_Contact,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Reports_Request':

        data = self.client.call(
            self.service,
            'createRequest',
            recipientContact,
            reason,
            reportType,
            requestorContact,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Reports.Request import Request
        return Request(data)


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'SoftLayer_Account_Reports_Request':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Reports.Request import Request
        return Request(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Reports_Request':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Reports.Request import Request
        return Request(data)


    def getRequestByRequestKey(
        self,
        requestKey: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Reports_Request':

        data = self.client.call(
            self.service,
            'getRequestByRequestKey',
            requestKey,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Reports.Request import Request
        return Request(data)


    def sendReportEmail(
        self,
        request: SoftLayer_Account_Reports_Request
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendReportEmail',
            request
        )
        
        return data


    def updateTicketOnDecline(
        self,
        request: SoftLayer_Account_Reports_Request
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateTicketOnDecline',
            request
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


    def getAccountContact(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact':

        data = self.client.call(
            self.service,
            'getAccountContact',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


    def getReportType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Compliance_Report_Type':

        data = self.client.call(
            self.service,
            'getReportType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Compliance.Report.Type import Type
        return Type(data)


    def getRequestorContact(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Contact':

        data = self.client.call(
            self.service,
            'getRequestorContact',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


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


