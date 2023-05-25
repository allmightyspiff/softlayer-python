from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Internal_Ibm_CostRecovery_Validator(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Internal_Ibm_CostRecovery_Validator'

    def getSprintContainer(self, accountId: str, countryId: str) -> 'Sprint_Container_CostRecovery':
        data = self.client.call('SoftLayer_Account_Internal_Ibm_CostRecovery_Validator', 'getSprintContainer', accountId, countryId)
        return data

    def validateByAccountAndCountryId(self, accountId: str, countryId: str) -> 'Sprint_Container_CostRecovery':
        data = self.client.call('SoftLayer_Account_Internal_Ibm_CostRecovery_Validator', 'validateByAccountAndCountryId', accountId, countryId)
        return data
