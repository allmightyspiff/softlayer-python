from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_MasterServiceAgreement(Entity):
    accountId: int
    guid: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_MasterServiceAgreement'

    def getFile(self) -> 'Container_Utility_File_Entity':
        """Get the user's accounts current MSA"""
        data = self.client.call('SoftLayer_Account_MasterServiceAgreement', 'getFile')
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data

    def getObject(self, identifier: int) -> 'Account_MasterServiceAgreement':
        """Retrieve a SoftLayer_Account_MasterServiceAgreement record."""
        data = self.client.call('SoftLayer_Account_MasterServiceAgreement', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_MasterServiceAgreement import Account_MasterServiceAgreement
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_MasterServiceAgreement', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data
