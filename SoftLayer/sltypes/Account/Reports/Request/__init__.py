from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Reports_Request(Entity):
    accountContactId: int
    accountId: int
    complianceReportTypeId: str
    createDate: datetime
    employeeRecordId: int
    id_: int
    modifyDate: datetime
    nda: str
    notes: str
    report: str
    requestKey: str
    requestorContactId: int
    status: str
    ticketId: int
    usrRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Reports_Request'

    def createRequest(self, recipientContact: 'Account_Contact', reason: str, reportType: str, requestorContact: 'Account_Contact') -> 'Account_Reports_Request':
        data = self.client.call('SoftLayer_Account_Reports_Request', 'createRequest', recipientContact, reason, reportType, requestorContact)
        return data

    def getAllObjects(self) -> 'Account_Reports_Request':
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Account_Reports_Request':
        """Retrieve a SoftLayer_Account_Reports_Request record."""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getObject', id=identifier)
        return data

    def getRequestByRequestKey(self, requestKey: str) -> 'Account_Reports_Request':
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getRequestByRequestKey', requestKey)
        return data

    def sendReportEmail(self, request: 'Account_Reports_Request') -> bool:
        data = self.client.call('SoftLayer_Account_Reports_Request', 'sendReportEmail', request)
        return data

    def updateTicketOnDecline(self, request: 'Account_Reports_Request') -> bool:
        data = self.client.call('SoftLayer_Account_Reports_Request', 'updateTicketOnDecline', request)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAccountContact(self, identifier: int) -> 'Account_Contact':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getAccountContact', id=identifier)
        from SoftLayer.sltypes.Account_Contact import Account_Contact
        return data

    def getReportType(self, identifier: int) -> 'Compliance_Report_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getReportType', id=identifier)
        from SoftLayer.sltypes.Compliance_Report_Type import Compliance_Report_Type
        return data

    def getRequestorContact(self, identifier: int) -> 'Account_Contact':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getRequestorContact', id=identifier)
        from SoftLayer.sltypes.Account_Contact import Account_Contact
        return data

    def getTicket(self, identifier: int) -> 'Ticket':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getTicket', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Reports_Request', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
