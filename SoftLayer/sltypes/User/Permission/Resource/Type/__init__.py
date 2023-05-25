from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Permission_Resource_Type(Entity):
    """These are the variables relating to SoftLayer_User_Permission_Resource_Type. Collectively they describe the
types of resources which can be linked to [[SoftLayer_User_Permission_Group]]."""
    className: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Permission_Resource_Type'

    def getAllObjects(self) -> list['User_Permission_Resource_Type']:
        """Retrieve an array of SoftLayer_User_Permission_Resource_Type objects."""
        data = self.client.call('SoftLayer_User_Permission_Resource_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'User_Permission_Resource_Type':
        """Retrieve a SoftLayer_User_Permission_Resource_Type record."""
        data = self.client.call('SoftLayer_User_Permission_Resource_Type', 'getObject', id=identifier)
        return data
