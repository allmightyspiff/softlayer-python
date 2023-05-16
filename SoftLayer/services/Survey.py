# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Survey(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Survey'
        self.client = client

    def getActiveSurveyByType(
        self,
        type: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Survey':

        data = self.client.call(
            self.service,
            'getActiveSurveyByType',
            type,
            mask=objectMask
        )
        from SoftLayer.datatypes.Survey import Survey
        return Survey(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Survey':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Survey import Survey
        return Survey(data)


    def takeSurvey(
        self,
        responses: SoftLayer_Survey_Response
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'takeSurvey',
            responses
        )
        
        return data


    def getQuestions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Survey_Question]':

        data = self.client.call(
            self.service,
            'getQuestions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Survey.Question import Question
        return Question(data)


    def getStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Survey_Status':

        data = self.client.call(
            self.service,
            'getStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Survey.Status import Status
        return Status(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Survey_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Survey.Type import Type
        return Type(data)


