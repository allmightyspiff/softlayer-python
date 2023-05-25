from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Info(Entity):
    """Every SoftLayer customer account has billing specific information which is kept in the SoftLayer_Billing_Info
data type. This information is used by the SoftLayer accounting group when sending invoices and making
billing inquiries."""
    accountId: int
    anniversaryDayOfMonth: int
    cardAccountNumber: str
    cardExpirationMonth: int
    cardExpirationYear: int
    cardNickname: str
    cardType: str
    cardVerificationNumber: str
    createDate: datetime
    id_: int
    lastFourPaymentCardDigits: int
    lastPaymentDate: datetime
    modifyDate: datetime
    paymentTerms: int
    percentDiscountOnetime: int
    percentDiscountRecurring: int
    sparePoolAmount: int
    taxCertificateId: str
    vatId: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Info'

    def getObject(self, identifier: int) -> 'Billing_Info':
        """Retrieve a SoftLayer_Billing_Info record."""
        data = self.client.call('SoftLayer_Billing_Info', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Info import Billing_Info
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAchInformation(self, identifier: int) -> list['Billing_Info_Ach']:
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getAchInformation', id=identifier)
        from SoftLayer.sltypes.Billing_Info_Ach import Billing_Info_Ach
        return data

    def getCurrency(self, identifier: int) -> 'Billing_Currency':
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getCurrency', id=identifier)
        from SoftLayer.sltypes.Billing_Currency import Billing_Currency
        return data

    def getCurrentBillingCycle(self, identifier: int) -> 'Billing_Info_Cycle':
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getCurrentBillingCycle', id=identifier)
        from SoftLayer.sltypes.Billing_Info_Cycle import Billing_Info_Cycle
        return data

    def getLastBillDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getLastBillDate', id=identifier)
        return data

    def getNextBillDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Billing_Info', 'getNextBillDate', id=identifier)
        return data
