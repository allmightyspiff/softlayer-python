from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket(Entity):
    """The SoftLayer_Ticket data type models a single SoftLayer customer support or notification ticket. Each ticket
object contains references to it's updates, the user it's assigned to, the SoftLayer department and employee
that it's assigned to, and any hardware objects or attached files associated with the ticket. Tickets are
described in further detail on the [[SoftLayer_Ticket]] service page.   To create a support ticket execute
the [[SoftLayer_Ticket::createStandardTicket|createStandardTicket]] or
[[SoftLayer_Ticket::createAdministrativeTicket|createAdministrativeTicket]] methods in the SoftLayer_Ticket
service. To create an upgrade ticket for the SoftLayer sales group execute the
[[SoftLayer_Ticket::createUpgradeTicket|createUpgradeTicket]]."""
    accountId: int
    assignedUserId: int
    billableFlag: bool
    bnppSupportedLocationId: int
    changeOwnerFlag: bool
    createDate: datetime
    euSupportedLocationId: int
    finalComments: str
    groupId: int
    id_: int
    lastEditDate: datetime
    lastEditType: str
    lastResponseDate: datetime
    locationId: int
    modifyDate: datetime
    notifyUserOnUpdateFlag: bool
    originatingIpAddress: str
    priority: int
    responsibleBrandId: int
    serverAdministrationBillingAmount: int
    serverAdministrationBillingInvoiceId: int
    serverAdministrationFlag: int
    serverAdministrationRefundInvoiceId: int
    serviceProviderId: int
    serviceProviderResourceId: str
    statusId: int
    subjectId: int
    title: str
    totalUpdateCount: int
    userEditableFlag: bool

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket'

    def addAssignedAgent(self, identifier: int, agentId: int) -> None:
        """Assign an Agent to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addAssignedAgent', agentId, id=identifier)
        return data

    def addAttachedAdditionalEmails(self, identifier: int, emails: str) -> bool:
        """Add non-user email addresses to a ticket's email notify list."""
        data = self.client.call('SoftLayer_Ticket', 'addAttachedAdditionalEmails', emails, id=identifier)
        return data

    def addAttachedDedicatedHost(self, identifier: int, dedicatedHostId: int) -> 'Ticket_Attachment_Dedicated_Host':
        """Attach a Dedicated Host to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addAttachedDedicatedHost', dedicatedHostId, id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment_Dedicated_Host import Ticket_Attachment_Dedicated_Host
        return data

    def addAttachedFile(self, identifier: int, fileAttachment: 'Container_Utility_File_Attachment') -> 'Ticket_Attachment_File':
        """Attach a file to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addAttachedFile', fileAttachment, id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment_File import Ticket_Attachment_File
        return data

    def addAttachedHardware(self, identifier: int, hardwareId: int) -> 'Ticket_Attachment_Hardware':
        """Attach hardware to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addAttachedHardware', hardwareId, id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment_Hardware import Ticket_Attachment_Hardware
        return data

    def addAttachedVirtualGuest(self, identifier: int, guestId: int, callCommit: bool) -> 'Ticket_Attachment_Virtual_Guest':
        """Attach a CloudLayer Computing Instance to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addAttachedVirtualGuest', guestId, callCommit, id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment_Virtual_Guest import Ticket_Attachment_Virtual_Guest
        return data

    def addFinalComments(self, identifier: int, finalComments: str) -> bool:
        """Add final comments to a closed ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addFinalComments', finalComments, id=identifier)
        return data

    def addScheduledAlert(self, identifier: int, activationTime: str) -> None:
        data = self.client.call('SoftLayer_Ticket', 'addScheduledAlert', activationTime, id=identifier)
        return data

    def addScheduledAutoClose(self, identifier: int, activationTime: str) -> None:
        data = self.client.call('SoftLayer_Ticket', 'addScheduledAutoClose', activationTime, id=identifier)
        return data

    def addUpdate(self, identifier: int, templateObject: 'Ticket_Update', attachedFiles: 'Container_Utility_File_Attachment') -> list['Ticket_Update']:
        """Add an update to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'addUpdate', templateObject, attachedFiles, id=identifier)
        from SoftLayer.sltypes.Ticket_Update import Ticket_Update
        return data

    def createAdministrativeTicket(self, templateObject: 'Ticket', contents: str, attachmentId: int, rootPassword: str, controlPanelPassword: str, accessPort: str, attachedFiles: 'Container_Utility_File_Attachment', attachmentType: str) -> 'Ticket':
        """Create an administrative support ticket."""
        data = self.client.call('SoftLayer_Ticket', 'createAdministrativeTicket', templateObject, contents, attachmentId, rootPassword, controlPanelPassword, accessPort, attachedFiles, attachmentType)
        return data

    def createCancelServerTicket(self, attachmentId: int, reason: str, content: str, cancelAssociatedItems: bool, attachmentType: str) -> 'Ticket':
        """Create a sales cancel server ticket to be cancelled on next bill date."""
        data = self.client.call('SoftLayer_Ticket', 'createCancelServerTicket', attachmentId, reason, content, cancelAssociatedItems, attachmentType)
        return data

    def createCancelServiceTicket(self, attachmentId: int, reason: str, content: str, attachmentType: str) -> 'Ticket':
        """Create a sales cancel service ticket."""
        data = self.client.call('SoftLayer_Ticket', 'createCancelServiceTicket', attachmentId, reason, content, attachmentType)
        return data

    def createStandardTicket(self, templateObject: 'Ticket', contents: str, attachmentId: int, rootPassword: str, controlPanelPassword: str, accessPort: str, attachedFiles: 'Container_Utility_File_Attachment', attachmentType: str) -> 'Ticket':
        """Create a standard support ticket."""
        data = self.client.call('SoftLayer_Ticket', 'createStandardTicket', templateObject, contents, attachmentId, rootPassword, controlPanelPassword, accessPort, attachedFiles, attachmentType)
        return data

    def createUpgradeTicket(self, attachmentId: int, genericUpgrade: str, upgradeMaintenanceWindow: str, details: str, attachmentType: str, title: str) -> 'Ticket':
        """Create an upgrade request ticket for the SoftLayer sales team."""
        data = self.client.call('SoftLayer_Ticket', 'createUpgradeTicket', attachmentId, genericUpgrade, upgradeMaintenanceWindow, details, attachmentType, title)
        return data

    def edit(self, identifier: int, templateObject: 'Ticket', contents: str, attachedFiles: 'Container_Utility_File_Attachment') -> 'Ticket':
        """Edit or update a SoftLayer ticket."""
        data = self.client.call('SoftLayer_Ticket', 'edit', templateObject, contents, attachedFiles, id=identifier)
        return data

    def getAllTicketGroups(self) -> list['Ticket_Group']:
        """Retrieve all available ticket groups."""
        data = self.client.call('SoftLayer_Ticket', 'getAllTicketGroups')
        from SoftLayer.sltypes.Ticket_Group import Ticket_Group
        return data

    def getAllTicketStatuses(self) -> list['Ticket_Status']:
        """Retrieve all available ticket statuses."""
        data = self.client.call('SoftLayer_Ticket', 'getAllTicketStatuses')
        from SoftLayer.sltypes.Ticket_Status import Ticket_Status
        return data

    def getAttachedFile(self, identifier: int, attachmentId: int) -> str:
        """Retrieve a file attached to a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedFile', attachmentId, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Ticket':
        """Retrieve a SoftLayer_Ticket record."""
        data = self.client.call('SoftLayer_Ticket', 'getObject', id=identifier)
        return data

    def getTicketsClosedSinceDate(self, closeDate: datetime) -> list['Ticket']:
        """Retrieve tickets closed since a given date."""
        data = self.client.call('SoftLayer_Ticket', 'getTicketsClosedSinceDate', closeDate)
        return data

    def markAsViewed(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Ticket', 'markAsViewed', id=identifier)
        return data

    def removeAssignedAgent(self, identifier: int, agentId: int) -> None:
        """Remove an assigned agent from a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'removeAssignedAgent', agentId, id=identifier)
        return data

    def removeAttachedAdditionalEmails(self, identifier: int, emails: str) -> bool:
        """Detaches non-user additional email addresses from a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'removeAttachedAdditionalEmails', emails, id=identifier)
        return data

    def removeAttachedHardware(self, identifier: int, hardwareId: int) -> bool:
        """detach hardware from a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'removeAttachedHardware', hardwareId, id=identifier)
        return data

    def removeAttachedVirtualGuest(self, identifier: int, guestId: int) -> bool:
        """Detach a CloudLayer Computing Instance from a ticket."""
        data = self.client.call('SoftLayer_Ticket', 'removeAttachedVirtualGuest', guestId, id=identifier)
        return data

    def removeScheduledAlert(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Ticket', 'removeScheduledAlert', id=identifier)
        return data

    def removeScheduledAutoClose(self, identifier: int) -> None:
        data = self.client.call('SoftLayer_Ticket', 'removeScheduledAutoClose', id=identifier)
        return data

    def setTags(self, identifier: int, tags: str) -> bool:
        data = self.client.call('SoftLayer_Ticket', 'setTags', tags, id=identifier)
        return data

    def surveyEligible(self) -> bool:
        data = self.client.call('SoftLayer_Ticket', 'surveyEligible')
        return data

    def updateAttachedAdditionalEmails(self, identifier: int, emails: str) -> bool:
        """Update non-user email addresses attached to a ticket's email notify list."""
        data = self.client.call('SoftLayer_Ticket', 'updateAttachedAdditionalEmails', emails, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAssignedAgents(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAssignedAgents', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getAssignedUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAssignedUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getAttachedAdditionalEmails(self, identifier: int) -> list['User_Customer_AdditionalEmail']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedAdditionalEmails', id=identifier)
        from SoftLayer.sltypes.User_Customer_AdditionalEmail import User_Customer_AdditionalEmail
        return data

    def getAttachedDedicatedHosts(self, identifier: int) -> list['Virtual_DedicatedHost']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedDedicatedHosts', id=identifier)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data

    def getAttachedFiles(self, identifier: int) -> list['Ticket_Attachment_File']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedFiles', id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment_File import Ticket_Attachment_File
        return data

    def getAttachedHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getAttachedHardwareCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedHardwareCount', id=identifier)
        return data

    def getAttachedResources(self, identifier: int) -> list['Ticket_Attachment']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedResources', id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment
        return data

    def getAttachedVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAttachedVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getAwaitingUserResponseFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getAwaitingUserResponseFlag', id=identifier)
        return data

    def getBnppSupportedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getBnppSupportedFlag', id=identifier)
        return data

    def getCancellationRequest(self, identifier: int) -> 'Billing_Item_Cancellation_Request':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getCancellationRequest', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request import Billing_Item_Cancellation_Request
        return data

    def getEmployeeAttachments(self, identifier: int) -> list['User_Employee']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getEmployeeAttachments', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getEuSupportedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getEuSupportedFlag', id=identifier)
        return data

    def getFirstAttachedResource(self, identifier: int) -> 'Ticket_Attachment':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getFirstAttachedResource', id=identifier)
        from SoftLayer.sltypes.Ticket_Attachment import Ticket_Attachment
        return data

    def getFirstUpdate(self, identifier: int) -> 'Ticket_Update':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getFirstUpdate', id=identifier)
        from SoftLayer.sltypes.Ticket_Update import Ticket_Update
        return data

    def getFsboaSupportedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getFsboaSupportedFlag', id=identifier)
        return data

    def getGroup(self, identifier: int) -> 'Ticket_Group':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getGroup', id=identifier)
        from SoftLayer.sltypes.Ticket_Group import Ticket_Group
        return data

    def getInvoiceItems(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getInvoiceItems', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getLastActivity(self, identifier: int) -> 'Ticket_Activity':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getLastActivity', id=identifier)
        from SoftLayer.sltypes.Ticket_Activity import Ticket_Activity
        return data

    def getLastEditor(self, identifier: int) -> 'User_Interface':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getLastEditor', id=identifier)
        from SoftLayer.sltypes.User_Interface import User_Interface
        return data

    def getLastUpdate(self, identifier: int) -> 'Ticket_Update':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getLastUpdate', id=identifier)
        from SoftLayer.sltypes.Ticket_Update import Ticket_Update
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getNewUpdatesFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getNewUpdatesFlag', id=identifier)
        return data

    def getScheduledActions(self, identifier: int) -> list['Provisioning_Version1_Transaction']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getScheduledActions', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getServerAdministrationBillingInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getServerAdministrationBillingInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getServerAdministrationRefundInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getServerAdministrationRefundInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getServiceProvider(self, identifier: int) -> 'Service_Provider':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getServiceProvider', id=identifier)
        from SoftLayer.sltypes.Service_Provider import Service_Provider
        return data

    def getState(self, identifier: int) -> list['Ticket_State']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getState', id=identifier)
        from SoftLayer.sltypes.Ticket_State import Ticket_State
        return data

    def getStatus(self, identifier: int) -> 'Ticket_Status':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Ticket_Status import Ticket_Status
        return data

    def getSubject(self, identifier: int) -> 'Ticket_Subject':
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getSubject', id=identifier)
        from SoftLayer.sltypes.Ticket_Subject import Ticket_Subject
        return data

    def getTagReferences(self, identifier: int) -> list['Tag_Reference']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getTagReferences', id=identifier)
        from SoftLayer.sltypes.Tag_Reference import Tag_Reference
        return data

    def getUpdateRatingFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getUpdateRatingFlag', id=identifier)
        return data

    def getUpdates(self, identifier: int) -> list['Ticket_Update']:
        """"""
        data = self.client.call('SoftLayer_Ticket', 'getUpdates', id=identifier)
        from SoftLayer.sltypes.Ticket_Update import Ticket_Update
        return data
