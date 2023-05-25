from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Package_Preset(Entity):
    """Package presets are used to simplify ordering by eliminating the need for price ids when submitting orders.
Orders submitted with a preset id defined will use the prices included in the package preset. Prices
submitted on an order with a preset id will replace the prices included in the package preset for that prices
category. If the package preset has a fixed configuration flag <em>(fixedConfigurationFlag)</em> set then the
prices included in the preset configuration cannot be replaced by prices submitted on the order. The only
exception to the fixed configuration flag would be if a price submitted on the order is an account-restricted
price for the same product item."""
    description: str
    id_: int
    isActive: str
    keyName: str
    name: str
    packageId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Package_Preset'

    def getAllObjects(self) -> list['Product_Package_Preset']:
        """Get all active package presets"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getAllObjects')
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getObject(self, identifier: int) -> 'Product_Package_Preset':
        """Retrieve a SoftLayer_Product_Package_Preset record."""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getAvailableStorageUnits(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getAvailableStorageUnits', id=identifier)
        return data

    def getBareMetalReservedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getBareMetalReservedFlag', id=identifier)
        return data

    def getCategories(self, identifier: int) -> list['Product_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getComputeGroup(self, identifier: int) -> 'Product_Item_Server_Group':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getComputeGroup', id=identifier)
        from SoftLayer.sltypes.Product_Item_Server_Group import Product_Item_Server_Group
        return data

    def getConfiguration(self, identifier: int) -> list['Product_Package_Preset_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getConfiguration', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset_Configuration import Product_Package_Preset_Configuration
        return data

    def getDisallowedComputeGroupUpgradeFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getDisallowedComputeGroupUpgradeFlag', id=identifier)
        return data

    def getFixedConfigurationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getFixedConfigurationFlag', id=identifier)
        return data

    def getLocations(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLowestPresetServerPrice(self, identifier: int) -> 'Product_Item_Price':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getLowestPresetServerPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getPackage(self, identifier: int) -> 'Product_Package':
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getPackage', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getPackageConfiguration(self, identifier: int) -> list['Product_Package_Order_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getPackageConfiguration', id=identifier)
        from SoftLayer.sltypes.Product_Package_Order_Configuration import Product_Package_Order_Configuration
        return data

    def getPrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getStorageGroupTemplateArrays(self, identifier: int) -> list['Configuration_Storage_Group_Template_Group']:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getStorageGroupTemplateArrays', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group_Template_Group import Configuration_Storage_Group_Template_Group
        return data

    def getTotalMinimumHourlyFee(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getTotalMinimumHourlyFee', id=identifier)
        return data

    def getTotalMinimumRecurringFee(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Product_Package_Preset', 'getTotalMinimumRecurringFee', id=identifier)
        return data
