from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Survey(Entity):
    """The SoftLayer_Survey data type contains general information relating to a single SoftLayer survey."""
    active: int
    createDate: datetime
    id_: int
    name: str
    statusId: int
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Survey'

    def getActiveSurveyByType(self, type_: str) -> 'Survey':
        """Provides survey details for the given type"""
        data = self.client.call('SoftLayer_Survey', 'getActiveSurveyByType', type)
        from SoftLayer.sltypes.Survey import Survey
        return data

    def getObject(self, identifier: int) -> 'Survey':
        """Retrieve a SoftLayer_Survey record."""
        data = self.client.call('SoftLayer_Survey', 'getObject', id=identifier)
        from SoftLayer.sltypes.Survey import Survey
        return data

    def takeSurvey(self, identifier: int, responses: 'Survey_Response') -> bool:
        """Respond to the questions that a survey has."""
        data = self.client.call('SoftLayer_Survey', 'takeSurvey', responses, id=identifier)
        return data

    def getQuestions(self, identifier: int) -> list['Survey_Question']:
        """"""
        data = self.client.call('SoftLayer_Survey', 'getQuestions', id=identifier)
        from SoftLayer.sltypes.Survey_Question import Survey_Question
        return data

    def getStatus(self, identifier: int) -> 'Survey_Status':
        """"""
        data = self.client.call('SoftLayer_Survey', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Survey_Status import Survey_Status
        return data

    def getType(self, identifier: int) -> 'Survey_Type':
        """"""
        data = self.client.call('SoftLayer_Survey', 'getType', id=identifier)
        from SoftLayer.sltypes.Survey_Type import Survey_Type
        return data
