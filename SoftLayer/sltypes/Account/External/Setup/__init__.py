from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_External_Setup(Entity):
    accountId: int
    currencyId: int
    id_: int
    serviceProviderId: int
    statusCode: str
    typeCode: str
    verifyCardTransactionId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_External_Setup'

    def finalizeExternalBillingForAccount(self, accountId: int) -> 'Container_Account_External_Setup_ProvisioningHoldLifted':
        data = self.client.call('SoftLayer_Account_External_Setup', 'finalizeExternalBillingForAccount', accountId)
        from SoftLayer.sltypes.Container_Account_External_Setup_ProvisioningHoldLifted import Container_Account_External_Setup_ProvisioningHoldLifted
        return data

    def getObject(self, identifier: int) -> 'Account_External_Setup':
        """Retrieve a SoftLayer_Account_External_Setup record."""
        data = self.client.call('SoftLayer_Account_External_Setup', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_External_Setup import Account_External_Setup
        return data

    def getVerifyCardTransaction(self, identifier: int) -> 'Billing_Payment_Card_Transaction':
        """"""
        data = self.client.call('SoftLayer_Account_External_Setup', 'getVerifyCardTransaction', id=identifier)
        from SoftLayer.sltypes.Billing_Payment_Card_Transaction import Billing_Payment_Card_Transaction
        return data
