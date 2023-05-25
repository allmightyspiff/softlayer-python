from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Security_Question(Entity):
    """The SoftLayer_User_Security_Question data type contains questions."""
    displayOrder: int
    id_: int
    question: str
    viewable: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Security_Question'

    def getAllObjects(self) -> list['User_Security_Question']:
        """Retrieve all viewable security questions."""
        data = self.client.call('SoftLayer_User_Security_Question', 'getAllObjects')
        from SoftLayer.sltypes.User_Security_Question import User_Security_Question
        return data

    def getObject(self, identifier: int) -> 'User_Security_Question':
        """Retrieve a SoftLayer_User_Security_Question record."""
        data = self.client.call('SoftLayer_User_Security_Question', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Security_Question import User_Security_Question
        return data
