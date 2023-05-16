# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addAssignedAgent(
        self,
        agentId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'addAssignedAgent',
            agentId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addAttachedAdditionalEmails(
        self,
        emails: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addAttachedAdditionalEmails',
            emails
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addAttachedDedicatedHost(
        self,
        dedicatedHostId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket_Attachment_Dedicated_Host':
        data = self.client.call(
            self.service,
            'addAttachedDedicatedHost',
            dedicatedHostId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Attachment.Dedicated.Host import Host
        return SL_Host(data)

# This file was automatically generated with tools/generateTypes.py
    def addAttachedFile(
        self,
        fileAttachment: SoftLayer_Container_Utility_File_Attachment,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket_Attachment_File':
        data = self.client.call(
            self.service,
            'addAttachedFile',
            fileAttachment,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Attachment.File import File
        return SL_File(data)

# This file was automatically generated with tools/generateTypes.py
    def addAttachedHardware(
        self,
        hardwareId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket_Attachment_Hardware':
        data = self.client.call(
            self.service,
            'addAttachedHardware',
            hardwareId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Attachment.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def addAttachedVirtualGuest(
        self,
        guestId: int,
        callCommit: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket_Attachment_Virtual_Guest':
        data = self.client.call(
            self.service,
            'addAttachedVirtualGuest',
            guestId,
            callCommit,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Attachment.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def addFinalComments(
        self,
        finalComments: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'addFinalComments',
            finalComments
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addScheduledAlert(
        self,
        activationTime: str
    ) -> 'void':
        data = self.client.call(
            self.service,
            'addScheduledAlert',
            activationTime
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addScheduledAutoClose(
        self,
        activationTime: str
    ) -> 'void':
        data = self.client.call(
            self.service,
            'addScheduledAutoClose',
            activationTime
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def addUpdate(
        self,
        templateObject: SoftLayer_Ticket_Update,
        attachedFiles: SoftLayer_Container_Utility_File_Attachment,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket_Update]':
        data = self.client.call(
            self.service,
            'addUpdate',
            templateObject,
            attachedFiles,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Update import Update
        return SL_Update(data)

# This file was automatically generated with tools/generateTypes.py
    def createAdministrativeTicket(
        self,
        templateObject: SoftLayer_Ticket,
        contents: str,
        attachmentId: int,
        rootPassword: str,
        controlPanelPassword: str,
        accessPort: str,
        attachedFiles: SoftLayer_Container_Utility_File_Attachment,
        attachmentType: enum,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'createAdministrativeTicket',
            templateObject,
            contents,
            attachmentId,
            rootPassword,
            controlPanelPassword,
            accessPort,
            attachedFiles,
            attachmentType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def createCancelServerTicket(
        self,
        attachmentId: int,
        reason: str,
        content: str,
        cancelAssociatedItems: boolean,
        attachmentType: enum,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'createCancelServerTicket',
            attachmentId,
            reason,
            content,
            cancelAssociatedItems,
            attachmentType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def createCancelServiceTicket(
        self,
        attachmentId: int,
        reason: str,
        content: str,
        attachmentType: enum,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'createCancelServiceTicket',
            attachmentId,
            reason,
            content,
            attachmentType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def createStandardTicket(
        self,
        templateObject: SoftLayer_Ticket,
        contents: str,
        attachmentId: int,
        rootPassword: str,
        controlPanelPassword: str,
        accessPort: str,
        attachedFiles: SoftLayer_Container_Utility_File_Attachment,
        attachmentType: enum,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'createStandardTicket',
            templateObject,
            contents,
            attachmentId,
            rootPassword,
            controlPanelPassword,
            accessPort,
            attachedFiles,
            attachmentType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def createUpgradeTicket(
        self,
        attachmentId: int,
        genericUpgrade: str,
        upgradeMaintenanceWindow: str,
        details: str,
        attachmentType: enum,
        title: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'createUpgradeTicket',
            attachmentId,
            genericUpgrade,
            upgradeMaintenanceWindow,
            details,
            attachmentType,
            title,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def edit(
        self,
        templateObject: SoftLayer_Ticket,
        contents: str,
        attachedFiles: SoftLayer_Container_Utility_File_Attachment,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'edit',
            templateObject,
            contents,
            attachedFiles,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllTicketGroups(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket_Group]':
        data = self.client.call(
            self.service,
            'getAllTicketGroups',
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllTicketStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket_Status]':
        data = self.client.call(
            self.service,
            'getAllTicketStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedFile(
        self,
        attachmentId: int
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getAttachedFile',
            attachmentId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def getTicketsClosedSinceDate(
        self,
        closeDate: dateTime,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket]':
        data = self.client.call(
            self.service,
            'getTicketsClosedSinceDate',
            closeDate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def markAsViewed(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'markAsViewed',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAssignedAgent(
        self,
        agentId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'removeAssignedAgent',
            agentId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAttachedAdditionalEmails(
        self,
        emails: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAttachedAdditionalEmails',
            emails
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAttachedHardware(
        self,
        hardwareId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAttachedHardware',
            hardwareId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeAttachedVirtualGuest(
        self,
        guestId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'removeAttachedVirtualGuest',
            guestId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeScheduledAlert(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'removeScheduledAlert',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def removeScheduledAutoClose(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'removeScheduledAutoClose',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def setTags(
        self,
        tags: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'setTags',
            tags
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def surveyEligible(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'surveyEligible',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def updateAttachedAdditionalEmails(
        self,
        emails: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'updateAttachedAdditionalEmails',
            emails
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
    def getAssignedAgents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':
        data = self.client.call(
            self.service,
            'getAssignedAgents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
    def getAssignedUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getAssignedUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedAdditionalEmails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer_AdditionalEmail]':
        data = self.client.call(
            self.service,
            'getAttachedAdditionalEmails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer.AdditionalEmail import AdditionalEmail
        return SL_AdditionalEmail(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedDedicatedHosts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_DedicatedHost]':
        data = self.client.call(
            self.service,
            'getAttachedDedicatedHosts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return SL_DedicatedHost(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedFiles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Attachment_File]':
        data = self.client.call(
            self.service,
            'getAttachedFiles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Attachment.File import File
        return SL_File(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getAttachedHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedHardwareCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':
        data = self.client.call(
            self.service,
            'getAttachedHardwareCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAttachedResources(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Attachment]':
        data = self.client.call(
            self.service,
            'getAttachedResources',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachedVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getAttachedVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)

# This file was automatically generated with tools/generateTypes.py
    def getAwaitingUserResponseFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getAwaitingUserResponseFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBnppSupportedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getBnppSupportedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCancellationRequest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Cancellation_Request':
        data = self.client.call(
            self.service,
            'getCancellationRequest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def getEmployeeAttachments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Employee]':
        data = self.client.call(
            self.service,
            'getEmployeeAttachments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return SL_Employee(data)

# This file was automatically generated with tools/generateTypes.py
    def getEuSupportedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getEuSupportedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getFirstAttachedResource(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Attachment':
        data = self.client.call(
            self.service,
            'getFirstAttachedResource',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getFirstUpdate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Update':
        data = self.client.call(
            self.service,
            'getFirstUpdate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Update import Update
        return SL_Update(data)

# This file was automatically generated with tools/generateTypes.py
    def getFsboaSupportedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getFsboaSupportedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Group':
        data = self.client.call(
            self.service,
            'getGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getInvoiceItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':
        data = self.client.call(
            self.service,
            'getInvoiceItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getLastActivity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Activity':
        data = self.client.call(
            self.service,
            'getLastActivity',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Activity import Activity
        return SL_Activity(data)

# This file was automatically generated with tools/generateTypes.py
    def getLastEditor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Interface':
        data = self.client.call(
            self.service,
            'getLastEditor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Interface import Interface
        return SL_Interface(data)

# This file was automatically generated with tools/generateTypes.py
    def getLastUpdate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Update':
        data = self.client.call(
            self.service,
            'getLastUpdate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Update import Update
        return SL_Update(data)

# This file was automatically generated with tools/generateTypes.py
    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getNewUpdatesFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getNewUpdatesFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getScheduledActions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Version1_Transaction]':
        data = self.client.call(
            self.service,
            'getScheduledActions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction import Transaction
        return SL_Transaction(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerAdministrationBillingInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':
        data = self.client.call(
            self.service,
            'getServerAdministrationBillingInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return SL_Invoice(data)

# This file was automatically generated with tools/generateTypes.py
    def getServerAdministrationRefundInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':
        data = self.client.call(
            self.service,
            'getServerAdministrationRefundInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return SL_Invoice(data)

# This file was automatically generated with tools/generateTypes.py
    def getServiceProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':
        data = self.client.call(
            self.service,
            'getServiceProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return SL_Provider(data)

# This file was automatically generated with tools/generateTypes.py
    def getState(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_State]':
        data = self.client.call(
            self.service,
            'getState',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.State import State
        return SL_State(data)

# This file was automatically generated with tools/generateTypes.py
    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Status':
        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getSubject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject':
        data = self.client.call(
            self.service,
            'getSubject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return SL_Subject(data)

# This file was automatically generated with tools/generateTypes.py
    def getTagReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag_Reference]':
        data = self.client.call(
            self.service,
            'getTagReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag.Reference import Reference
        return SL_Reference(data)

# This file was automatically generated with tools/generateTypes.py
    def getUpdateRatingFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getUpdateRatingFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getUpdates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Update]':
        data = self.client.call(
            self.service,
            'getUpdates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Update import Update
        return SL_Update(data)


