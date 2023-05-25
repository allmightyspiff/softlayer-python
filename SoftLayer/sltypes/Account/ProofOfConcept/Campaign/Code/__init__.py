from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept_Campaign_Code(Entity):
    """A [SoftLayer_Account_ProofOfConcept_Campaign_Code] provides a `code` and an optional `description`."""
    code: str
    description: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept_Campaign_Code'

    def getAllObjects(self) -> list['Account_ProofOfConcept_Campaign_Code']:
        """Get all Proof of Concept campaign codes."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Campaign_Code', 'getAllObjects')
        from SoftLayer.sltypes.Account_ProofOfConcept_Campaign_Code import Account_ProofOfConcept_Campaign_Code
        return data

    def getObject(self, identifier: int) -> 'Account_ProofOfConcept_Campaign_Code':
        """Retrieve a SoftLayer_Account_ProofOfConcept_Campaign_Code record."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Campaign_Code', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Campaign_Code import Account_ProofOfConcept_Campaign_Code
        return data
