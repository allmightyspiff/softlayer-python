from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Address_Type(Entity):
    createDate: datetime
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Address_Type'

    def getObject(self, identifier: int) -> 'Account_Address_Type':
        """Retrieve a SoftLayer_Account_Address_Type record."""
        data = self.client.call('SoftLayer_Account_Address_Type', 'getObject', id=identifier)
        return data
