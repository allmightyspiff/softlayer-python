# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Update_Employee(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Update_Employee'
        self.client = client

    def addResponseRating(
        self,
        responseRating: int,
        responseIndex: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addResponseRating',
            responseRating,
            responseIndex
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Update_Employee':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Update.Employee import Employee
        return Employee(data)


    def getChangeOwnerActivity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getChangeOwnerActivity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getChat(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Chat_Liveperson':

        data = self.client.call(
            self.service,
            'getChat',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Chat.Liveperson import Liveperson
        return Liveperson(data)


    def getEditor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Interface':

        data = self.client.call(
            self.service,
            'getEditor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Interface import Interface
        return Interface(data)


    def getFileAttachment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Attachment_File]':

        data = self.client.call(
            self.service,
            'getFileAttachment',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Attachment.File import File
        return File(data)


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


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Update_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Update.Type import Type
        return Type(data)


