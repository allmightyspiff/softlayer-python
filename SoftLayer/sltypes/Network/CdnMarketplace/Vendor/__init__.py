from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_CdnMarketplace_Vendor(Entity):
    """The SoftLayer_Network_CdnMarketplace_Vendor contains information regarding\u2028 a CDN Vendor. This class is
associated with\u2028 SoftLayer_Network_CdnMarketplace_Vendor_Attribute class."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_CdnMarketplace_Vendor'

    def getObject(self, identifier: int) -> 'Network_CdnMarketplace_Vendor':
        """Retrieve a SoftLayer_Network_CdnMarketplace_Vendor record."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Vendor', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_CdnMarketplace_Vendor import Network_CdnMarketplace_Vendor
        return data

    def listVendors(self) -> list['Container_Network_CdnMarketplace_Vendor']:
        """SOAP API will return all CDN vendors available."""
        data = self.client.call('SoftLayer_Network_CdnMarketplace_Vendor', 'listVendors')
        from SoftLayer.sltypes.Container_Network_CdnMarketplace_Vendor import Container_Network_CdnMarketplace_Vendor
        return data
