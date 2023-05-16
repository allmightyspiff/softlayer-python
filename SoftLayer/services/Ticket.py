# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket'
        self.client = client

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
        return Host(data)


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
        return File(data)


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
        return Hardware(data)


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
        return Guest(data)


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
        return Update(data)


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
        return Ticket(data)


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
        return Ticket(data)


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
        return Ticket(data)


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
        return Ticket(data)


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
        return Ticket(data)


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
        return Ticket(data)


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
        return Group(data)


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
        return Status(data)


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
        return Ticket(data)


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
        return Ticket(data)


    def markAsViewed(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'markAsViewed',
            
        )
        
        return data


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


    def removeScheduledAlert(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeScheduledAlert',
            
        )
        
        return data


    def removeScheduledAutoClose(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'removeScheduledAutoClose',
            
        )
        
        return data


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


    def surveyEligible(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'surveyEligible',
            
        )
        
        return data


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
        return Customer(data)


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
        return Customer(data)


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
        return AdditionalEmail(data)


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
        return DedicatedHost(data)


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
        return File(data)


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
        return Hardware(data)


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
        return Attachment(data)


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
        return Guest(data)


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
        return Request(data)


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
        return Employee(data)


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
        return Attachment(data)


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
        return Update(data)


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
        return Group(data)


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
        return Item(data)


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
        return Activity(data)


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
        return Interface(data)


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
        return Update(data)


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
        return Location(data)


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
        return Transaction(data)


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
        return Invoice(data)


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
        return Invoice(data)


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
        return Provider(data)


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
        return State(data)


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
        return Status(data)


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
        return Subject(data)


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
        return Reference(data)


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
        return Update(data)


