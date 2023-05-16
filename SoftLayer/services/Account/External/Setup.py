# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_External_Setup(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_External_Setup'
        self.client = client

    def finalizeExternalBillingForAccount(
        self,
        accountId: int
    ) -> 'SoftLayer_Container_Account_External_Setup_ProvisioningHoldLifted':

        data = self.client.call(
            self.service,
            'finalizeExternalBillingForAccount',
            accountId
        )
        from SoftLayer.datatypes.Container.Account.External.Setup.ProvisioningHoldLifted import ProvisioningHoldLifted
        return ProvisioningHoldLifted(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_External_Setup':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.External.Setup import Setup
        return Setup(data)


    def getVerifyCardTransaction(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Payment_Card_Transaction':

        data = self.client.call(
            self.service,
            'getVerifyCardTransaction',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Payment.Card.Transaction import Transaction
        return Transaction(data)


