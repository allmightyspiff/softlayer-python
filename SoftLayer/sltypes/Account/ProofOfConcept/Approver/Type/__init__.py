from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept_Approver_Type(Entity):
    """This class represents a Proof of Concept account approver type."""
    description: str
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept_Approver_Type'

    def getObject(self, identifier: int) -> 'Account_ProofOfConcept_Approver_Type':
        """Retrieve a SoftLayer_Account_ProofOfConcept_Approver_Type record."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver_Type import Account_ProofOfConcept_Approver_Type
        return data

    def getApprovers(self, identifier: int) -> list['Account_ProofOfConcept_Approver']:
        """"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver_Type', 'getApprovers', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver import Account_ProofOfConcept_Approver
        return data
