from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Permission_Action(Entity):
    """The SoftLayer_User_Permission_Action data type contains local attributes to identify and describe the valid
actions a customer user can perform within IMS.  This includes a name, key name, and description.  This data
can not be modified by users of IMS.   It also contains relational attributes that indicate which
SoftLayer_User_Permission_Group's include the action."""
    createDate: datetime
    description: str
    id_: int
    key: str
    keyName: str
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Permission_Action'

    def getAllObjects(self) -> list['User_Permission_Action']:
        """Retrieve all customer permission actions in IMS."""
        data = self.client.call('SoftLayer_User_Permission_Action', 'getAllObjects')
        from SoftLayer.sltypes.User_Permission_Action import User_Permission_Action
        return data

    def getObject(self, identifier: int) -> 'User_Permission_Action':
        """Retrieve a SoftLayer_User_Permission_Action record."""
        data = self.client.call('SoftLayer_User_Permission_Action', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Permission_Action import User_Permission_Action
        return data
