from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept_Approver_Role(Entity):
    """This class represents a Proof of Concept account approver type. The current roles are Primary and Backup
approvers."""
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept_Approver_Role'

    def getObject(self, identifier: int) -> 'Account_ProofOfConcept_Approver_Role':
        """Retrieve a SoftLayer_Account_ProofOfConcept_Approver_Role record."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver_Role', 'getObject', id=identifier)
        return data
