from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Agreement(Entity):
    agreementTypeId: int
    autoRenew: int
    cancellationFee: int
    createDate: datetime
    durationMonths: int
    endDate: datetime
    id_: int
    startDate: datetime
    statusId: int
    title: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Agreement'

    def getObject(self, identifier: int) -> 'Account_Agreement':
        """Retrieve a SoftLayer_Account_Agreement record."""
        data = self.client.call('SoftLayer_Account_Agreement', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAgreementType(self, identifier: int) -> 'Account_Agreement_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getAgreementType', id=identifier)
        from SoftLayer.sltypes.Account_Agreement_Type import Account_Agreement_Type
        return data

    def getAttachedBillingAgreementFiles(self, identifier: int) -> list['Account_MasterServiceAgreement']:
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getAttachedBillingAgreementFiles', id=identifier)
        from SoftLayer.sltypes.Account_MasterServiceAgreement import Account_MasterServiceAgreement
        return data

    def getBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getStatus(self, identifier: int) -> 'Account_Agreement_Status':
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Account_Agreement_Status import Account_Agreement_Status
        return data

    def getTopLevelBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account_Agreement', 'getTopLevelBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data
