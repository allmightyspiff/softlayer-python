from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Security_Answer(Entity):
    """The SoftLayer_User_Customer_Security_Answer type contains user's answers to security questions."""
    answer: str
    id_: int
    questionId: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Security_Answer'

    def getObject(self, identifier: int) -> 'User_Customer_Security_Answer':
        """Retrieve a SoftLayer_User_Customer_Security_Answer record."""
        data = self.client.call('SoftLayer_User_Customer_Security_Answer', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_Security_Answer import User_Customer_Security_Answer
        return data

    def getQuestion(self, identifier: int) -> 'User_Security_Question':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Security_Answer', 'getQuestion', id=identifier)
        from SoftLayer.sltypes.User_Security_Question import User_Security_Question
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_Security_Answer', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
