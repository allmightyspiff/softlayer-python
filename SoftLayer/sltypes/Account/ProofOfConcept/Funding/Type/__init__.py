from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept_Funding_Type(Entity):
    keyName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept_Funding_Type'

    def getAllObjects(self) -> list['Account_ProofOfConcept_Funding_Type']:
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Funding_Type', 'getAllObjects')
        from SoftLayer.sltypes.Account_ProofOfConcept_Funding_Type import Account_ProofOfConcept_Funding_Type
        return data

    def getObject(self, identifier: int) -> 'Account_ProofOfConcept_Funding_Type':
        """Retrieve a SoftLayer_Account_ProofOfConcept_Funding_Type record."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Funding_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Funding_Type import Account_ProofOfConcept_Funding_Type
        return data

    def getApproverTypes(self, identifier: int) -> list['Account_ProofOfConcept_Approver_Type']:
        """"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Funding_Type', 'getApproverTypes', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver_Type import Account_ProofOfConcept_Approver_Type
        return data

    def getApprovers(self, identifier: int) -> list['Account_ProofOfConcept_Approver']:
        """"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept_Funding_Type', 'getApprovers', id=identifier)
        from SoftLayer.sltypes.Account_ProofOfConcept_Approver import Account_ProofOfConcept_Approver
        return data
