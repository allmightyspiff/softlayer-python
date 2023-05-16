# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Security_Question(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Security_Question'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_User_Security_Question]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Security.Question import Question
        return Question(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Security_Question':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Security.Question import Question
        return Question(data)


