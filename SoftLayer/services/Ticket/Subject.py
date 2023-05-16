# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Subject(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Subject'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Subject(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return SL_Subject(data)

# This file was automatically generated with tools/generateTypes.py
    def getTopFiveKnowledgeLayerQuestions(
        self,
        
    ) -> 'list[SoftLayer_Container_KnowledgeLayer_QuestionAnswer]':
        data = self.client.call(
            self.service,
            'getTopFiveKnowledgeLayerQuestions',
            
        )
        from SoftLayer.datatypes.Container.KnowledgeLayer.QuestionAnswer import QuestionAnswer
        return SL_QuestionAnswer(data)

# This file was automatically generated with tools/generateTypes.py
    def getCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject_Category':
        data = self.client.call(
            self.service,
            'getCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject.Category import Category
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
    def getChildren(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Subject]':
        data = self.client.call(
            self.service,
            'getChildren',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return SL_Subject(data)

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
    def getParent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Ticket_Subject':
        data = self.client.call(
            self.service,
            'getParent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return SL_Subject(data)


