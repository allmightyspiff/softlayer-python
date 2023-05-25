from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_CustomerPermission_Permission(Entity):
    """Each SoftLayer portal account is assigned a series of permissions that determine what access the user has to
functions within the SoftLayer customer portal. This status is reflected in the
SoftLayer_User_Customer_Status data type. Permissions differ from user status in that user status applies
globally to the portal while user permissions are applied to specific portal functions."""
    key: str
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_CustomerPermission_Permission'

    def getAllObjects(self) -> list['User_Customer_CustomerPermission_Permission']:
        """Retrieve all available permissions."""
        data = self.client.call('SoftLayer_User_Customer_CustomerPermission_Permission', 'getAllObjects')
        from SoftLayer.sltypes.User_Customer_CustomerPermission_Permission import User_Customer_CustomerPermission_Permission
        return data

    def getObject(self, identifier: int) -> 'User_Customer_CustomerPermission_Permission':
        """Retrieve a SoftLayer_User_Customer_CustomerPermission_Permission record."""
        data = self.client.call('SoftLayer_User_Customer_CustomerPermission_Permission', 'getObject', id=identifier)
        from SoftLayer.sltypes.User_Customer_CustomerPermission_Permission import User_Customer_CustomerPermission_Permission
        return data
