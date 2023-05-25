from SoftLayer.sltypes.Account.Link import Account_Link
from SoftLayer.sltypes.Account_Link import Account_Link
from SoftLayer import BaseClient

class Account_Link_Bluemix(Account_Link):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Link_Bluemix'

    def getObject(self, identifier: int) -> 'Account_Link_Bluemix':
        """Retrieve a SoftLayer_Account_Link_Bluemix record."""
        data = self.client.call('SoftLayer_Account_Link_Bluemix', 'getObject', id=identifier)
        return data

    def getSupportTierType(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Account_Link_Bluemix', 'getSupportTierType', id=identifier)
        return data
