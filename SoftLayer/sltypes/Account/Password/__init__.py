from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Password(Entity):
    """The SoftLayer_Account_Password contains username, passwords and notes for services that may require for
external applications such the Webcc interface for the EVault Storage service."""
    accountId: int
    id_: int
    notes: str
    password: str
    typeId: int
    username: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Password'

    def editObject(self, identifier: int, templateObject: 'Account_Password') -> bool:
        """Edit the password and/or notes for an account password."""
        data = self.client.call('SoftLayer_Account_Password', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Account_Password':
        """Retrieve a SoftLayer_Account_Password record."""
        data = self.client.call('SoftLayer_Account_Password', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Password import Account_Password
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Password', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getType(self, identifier: int) -> 'Account_Password_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Password', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Password_Type import Account_Password_Type
        return data
