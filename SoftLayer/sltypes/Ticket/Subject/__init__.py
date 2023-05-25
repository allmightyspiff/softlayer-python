from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Ticket_Subject(Entity):
    """The SoftLayer_Ticket_Subject data type models one of the possible subjects that a standard support ticket may
belong to. A basic support ticket's title matches it's corresponding subject's name."""
    categoryId: int
    id_: int
    name: str
    parentId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Ticket_Subject'

    def getAllObjects(self) -> list['Ticket_Subject']:
        """Retrieve all ticket subjects."""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Ticket_Subject':
        """Retrieve a SoftLayer_Ticket_Subject record."""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getObject', id=identifier)
        return data

    def getTopFiveKnowledgeLayerQuestions(self, identifier: int) -> list['Container_KnowledgeLayer_QuestionAnswer']:
        """Retrieve the top five KnowledgeLayer questions for a ticket subject"""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getTopFiveKnowledgeLayerQuestions', id=identifier)
        from SoftLayer.sltypes.Container_KnowledgeLayer_QuestionAnswer import Container_KnowledgeLayer_QuestionAnswer
        return data

    def getCategory(self, identifier: int) -> 'Ticket_Subject_Category':
        """"""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getCategory', id=identifier)
        from SoftLayer.sltypes.Ticket_Subject_Category import Ticket_Subject_Category
        return data

    def getChildren(self, identifier: int) -> list['Ticket_Subject']:
        """"""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getChildren', id=identifier)
        return data

    def getGroup(self, identifier: int) -> 'Ticket_Group':
        """"""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getGroup', id=identifier)
        from SoftLayer.sltypes.Ticket_Group import Ticket_Group
        return data

    def getParent(self, identifier: int) -> 'Ticket_Subject':
        """"""
        data = self.client.call('SoftLayer_Ticket_Subject', 'getParent', id=identifier)
        return data
