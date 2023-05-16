# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Security_Answer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Security_Answer'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Answer(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Question(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Customer(data)


