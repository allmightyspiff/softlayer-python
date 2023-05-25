from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Authentication_Attribute_Type(Entity):
    """SoftLayer_Account_Authentication_Attribute_Type models the type of attribute that can be assigned to a
SoftLayer customer account authentication."""
    description: str
    id_: int
    keyName: str
    name: str
    valueExample: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Authentication_Attribute_Type'

    def getAllObjects(self) -> list['Account_Attribute_Type']:
        data = self.client.call('SoftLayer_Account_Authentication_Attribute_Type', 'getAllObjects')
        from SoftLayer.sltypes.Account_Attribute_Type import Account_Attribute_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Authentication_Attribute_Type':
        """Retrieve a SoftLayer_Account_Authentication_Attribute_Type record."""
        data = self.client.call('SoftLayer_Account_Authentication_Attribute_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Attribute_Type import Account_Authentication_Attribute_Type
        return data
