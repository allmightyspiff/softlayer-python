from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_ApiAuthentication(Entity):
    """The SoftLayer_User_Customer_ApiAuthentication type contains user's authentication key(s)."""
    authenticationKey: str
    id_: int
    ipAddressRestriction: str
    timestampKey: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_ApiAuthentication'

    def editObject(self, identifier: int, templateObject: 'User_Customer_ApiAuthentication') -> 'User_Customer_ApiAuthentication':
        """Edit customer ApiAuthentication record."""
        data = self.client.call('SoftLayer_User_Customer_ApiAuthentication', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'User_Customer_ApiAuthentication':
        """Retrieve a SoftLayer_User_Customer_ApiAuthentication record."""
        data = self.client.call('SoftLayer_User_Customer_ApiAuthentication', 'getObject', id=identifier)
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_User_Customer_ApiAuthentication', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
