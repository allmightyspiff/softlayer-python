from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Software_AccountLicense(Entity):
    """SoftLayer_Software_AccountLicense is a class that represents software licenses that are tied only to a
customer's account and not to any particular hardware, IP address, etc."""
    accountId: int
    capacity: str
    key: str
    units: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_AccountLicense'

    def getAllObjects(self) -> list['Software_AccountLicense']:
        """Return all account licenses"""
        data = self.client.call('SoftLayer_Software_AccountLicense', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Software_AccountLicense':
        """Retrieve a SoftLayer_Software_AccountLicense record."""
        data = self.client.call('SoftLayer_Software_AccountLicense', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Software_AccountLicense', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Software_AccountLicense', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Software_AccountLicense', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data
