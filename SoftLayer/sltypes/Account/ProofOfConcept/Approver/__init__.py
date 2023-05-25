from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept_Approver(Entity):
    """This class represents a Proof of Concept account approver."""
    approvalOrder: int
    bluepagesUid: str
    email: str
    firstName: str
    id_: int
    lastName: str
    regionKeyName: str
    roleId: int
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept_Approver'

    def getAllObjects(self) -> list['Account_ProofOfConcept_Approver']:
        """Retrieves a list of reviewers"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver', 'getAllObjects')
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver import Account_ProofOfConcept_Approver
        return data

    def getObject(self, identifier: int) -> 'Account_ProofOfConcept_Approver':
        """Retrieve a SoftLayer_Account_ProofOfConcept_Approver record."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver import Account_ProofOfConcept_Approver
        return data

    def getRole(self, identifier: int) -> 'Account_ProofOfConcept_Approver_Role':
        """"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver', 'getRole', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver_Role import Account_ProofOfConcept_Approver_Role
        return data

    def getType(self, identifier: int) -> 'Account_ProofOfConcept_Approver_Type':
        """"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Approver', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver_Type import Account_ProofOfConcept_Approver_Type
        return data
