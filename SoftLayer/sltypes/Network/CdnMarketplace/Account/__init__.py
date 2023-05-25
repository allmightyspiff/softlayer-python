from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Account(Entity):
    """The SoftLayer_Network_CdnMarketplace_Account data type models an individual CDN account. CDN accounts contain
the SoftLayer account ID of the customer, the vendor ID the account belongs to, the customer ID provided by
the vendor, and a CDN account's status."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Account'

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Account':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Account record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Account', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Account import Network_CdnMarketplace_Account
        return data

    def verifyCdnAccountExists(self, vendorName: str) -> bool:
        """Wrapper for UI to verify whether or not an account exists for user under specified vendor. Returns true if
account exists, else false."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Account', 'verifyCdnAccountExists', vendorName)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Account', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Account', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data
