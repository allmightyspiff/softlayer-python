from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Brand_Migration_Request(Entity):
    """Represents a request to migrate an account to the owned brand."""
    accountId: int
    createDate: datetime
    destinationBrandId: int
    id_: int
    migrationDate: datetime
    modifyDate: datetime
    sourceBrandId: int
    status: str
    statusMessage: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Brand_Migration_Request'

    def getObject(self, identifier: int) -> 'Account_Brand_Migration_Request':
        """Retrieve a SoftLayer_Account_Brand_Migration_Request record."""
        data = self.client.call('SoftLayer_Account_Brand_Migration_Request', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Brand_Migration_Request import Account_Brand_Migration_Request
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Brand_Migration_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDestinationBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Account_Brand_Migration_Request', 'getDestinationBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getSourceBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Account_Brand_Migration_Request', 'getSourceBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Brand_Migration_Request', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
