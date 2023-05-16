# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Attachment_File_ServiceNow(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Attachment_File_ServiceNow'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Attachment_File_ServiceNow':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Attachment.File.ServiceNow import ServiceNow
        return ServiceNow(data)


    def getExtensionWhitelist(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getExtensionWhitelist',
            
        )
        
        return data


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


    def getUpdate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Update':

        data = self.client.call(
            self.service,
            'getUpdate',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Update import Update
        return Update(data)


