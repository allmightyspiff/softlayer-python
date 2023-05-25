from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Permission_Group_Type(Entity):
    """These are the attributes which describe a SoftLayer_User_Permission_Group_Type. All
SoftLayer_User_Permission_Group objects must be linked to one of these types.   For further information see:
[[SoftLayer_User_Permission_Group]]."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Permission_Group_Type'

    def getObject(self, identifier: int) -> 'User_Permission_Group_Type':
        """Retrieve a SoftLayer_User_Permission_Group_Type record."""
        data = self.client.call('SoftLayer_User_Permission_Group_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group_Type import User_Permission_Group_Type
        return data

    def getGroups(self, identifier: int) -> list['User_Permission_Group']:
        """"""
        data = self.client.call('SoftLayer_User_Permission_Group_Type', 'getGroups', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data
