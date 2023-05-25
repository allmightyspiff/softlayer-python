from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Authentication_Attribute(Entity):
    """Account authentication has many different settings that can be set. This class allows the customer or
employee to set these settings."""
    accountId: int
    id_: int
    typeId: int
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Authentication_Attribute'

    def getObject(self, identifier: int) -> 'Account_Authentication_Attribute':
        """Retrieve a SoftLayer_Account_Authentication_Attribute record."""
        data = self.client.call('SoftLayer_Account_Authentication_Attribute', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Authentication_Attribute', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAuthenticationRecord(self, identifier: int) -> 'Account_Authentication_Saml':
        """"""
        data = self.client.call('SoftLayer_Account_Authentication_Attribute', 'getAuthenticationRecord', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Saml import Account_Authentication_Saml
        return data

    def getType(self, identifier: int) -> 'Account_Authentication_Attribute_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Authentication_Attribute', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Attribute_Type import Account_Authentication_Attribute_Type
        return data
