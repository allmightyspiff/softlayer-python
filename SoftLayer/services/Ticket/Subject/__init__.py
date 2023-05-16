# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Subject(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Subject'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Subject]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return Subject(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return Subject(data)


    def getTopFiveKnowledgeLayerQuestions(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_KnowledgeLayer_QuestionAnswer]':

        data = self.client.call(
            self.service,
            'getTopFiveKnowledgeLayerQuestions',
            id=identifier
        )
        from SoftLayer.datatypes.Container.KnowledgeLayer.QuestionAnswer import QuestionAnswer
        return QuestionAnswer(data)


    def getCategory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject_Category':

        data = self.client.call(
            self.service,
            'getCategory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject.Category import Category
        return Category(data)


    def getChildren(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Subject]':

        data = self.client.call(
            self.service,
            'getChildren',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return Subject(data)


    def getGroup(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Group':

        data = self.client.call(
            self.service,
            'getGroup',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Group import Group
        return Group(data)


    def getParent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject':

        data = self.client.call(
            self.service,
            'getParent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return Subject(data)


