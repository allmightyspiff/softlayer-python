# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Security_Answer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Security_Answer'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer_Security_Answer':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer.Security.Answer import Answer
        return Answer(data)


    def getQuestion(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Security_Question':

        data = self.client.call(
            self.service,
            'getQuestion',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Security.Question import Question
        return Question(data)


    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


