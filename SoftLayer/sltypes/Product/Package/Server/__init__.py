from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Package_Server(Entity):
    """The SoftLayer_Product_Package_Server data type contains summarized information for bare metal servers
regarding pricing, processor stats, and feature sets."""
    bareMetalReservedFlag: bool
    catalogId: int
    datacenters: str
    defaultRamCapacity: float
    dualPathNetworkFlag: bool
    flexCoreServerFlag: bool
    gpuFlag: bool
    hourlyBillingFlag: bool
    id_: int
    itemId: int
    itemPriceId: int
    maximumDriveCount: int
    maximumPortSpeed: float
    maximumRamCapacity: float
    minimumPortSpeed: float
    networkGatewayApplianceRoleFlag: bool
    outletFlag: bool
    packageId: int
    packageType: str
    powerServerFlag: bool
    presetId: int
    privateNetworkOnlyFlag: bool
    processorBusSpeed: str
    processorCache: str
    processorCores: int
    processorCount: int
    processorManufacturer: str
    processorModel: str
    processorName: str
    processorSpeed: str
    productName: str
    redundantPowerFlag: bool
    sapCertifiedServerFlag: bool
    startingHourlyPrice: float
    startingMonthlyPrice: float
    termLength: int
    totalCoreCount: int
    txtTpmFlag: bool
    unitSize: int
    vmwareVsanNodeFlag: bool

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Package_Server'

    def getAllObjects(self) -> list['Product_Package_Server']:
        """Get the package servers"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Product_Package_Server':
        """Retrieve a SoftLayer_Product_Package_Server record."""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getObject', id=identifier)
        return data

    def getCatalog(self, identifier: int) -> 'Product_Catalog':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getCatalog', id=identifier)
        from SoftLayer.sltypes.Product_Catalog import Product_Catalog
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getItemPrice(self, identifier: int) -> 'Product_Item_Price':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getItemPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getPackage(self, identifier: int) -> 'Product_Package':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getPackage', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getPreset(self, identifier: int) -> 'Product_Package_Preset':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Server', 'getPreset', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data
