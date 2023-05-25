from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item(Entity):
    """The SoftLayer_Product_Item data type contains general information relating to a single SoftLayer product."""
    capacity: float
    description: str
    hardwareGenericComponentId: int
    id_: int
    itemTaxCategoryId: int
    keyName: str
    longDescription: str
    softwareDescriptionId: int
    units: str
    upgradeItemId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item'

    def getObject(self, identifier: int) -> 'Product_Item':
        """Retrieve a SoftLayer_Product_Item record."""
        data = self.client.call('SoftLayer_Product_Item', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getActivePresaleEvents(self, identifier: int) -> list['Sales_Presale_Event']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getActivePresaleEvents', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getActiveUsagePrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getActiveUsagePrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAttributes(self, identifier: int) -> list['Product_Item_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Product_Item_Attribute import Product_Item_Attribute
        return data

    def getAvailabilityAttributes(self, identifier: int) -> list['Product_Item_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getAvailabilityAttributes', id=identifier)
        from SoftLayer.sltypes.Product_Item_Attribute import Product_Item_Attribute
        return data

    def getBillingType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getBillingType', id=identifier)
        return data

    def getBundle(self, identifier: int) -> list['Product_Item_Bundles']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getBundle', id=identifier)
        from SoftLayer.sltypes.Product_Item_Bundles import Product_Item_Bundles
        return data

    def getBundleItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getBundleItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getCapacityMaximum(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getCapacityMaximum', id=identifier)
        return data

    def getCapacityMinimum(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getCapacityMinimum', id=identifier)
        return data

    def getCapacityRestrictedProductFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getCapacityRestrictedProductFlag', id=identifier)
        return data

    def getCategories(self, identifier: int) -> list['Product_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getConfigurationTemplates(self, identifier: int) -> list['Configuration_Template']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getConfigurationTemplates', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def getConflicts(self, identifier: int) -> list['Product_Item_Resource_Conflict']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getConflicts', id=identifier)
        from SoftLayer.sltypes.Product_Item_Resource_Conflict import Product_Item_Resource_Conflict
        return data

    def getCoreRestrictedItemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getCoreRestrictedItemFlag', id=identifier)
        return data

    def getDowngradeItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getDowngradeItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getDowngradeItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getDowngradeItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getGlobalCategoryConflicts(self, identifier: int) -> list['Product_Item_Resource_Conflict']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getGlobalCategoryConflicts', id=identifier)
        from SoftLayer.sltypes.Product_Item_Resource_Conflict import Product_Item_Resource_Conflict
        return data

    def getHardwareGenericComponentModel(self, identifier: int) -> 'Hardware_Component_Model_Generic':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getHardwareGenericComponentModel', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Generic import Hardware_Component_Model_Generic
        return data

    def getHideFromPortalFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getHideFromPortalFlag', id=identifier)
        return data

    def getIneligibleForAccountDiscountFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getIneligibleForAccountDiscountFlag', id=identifier)
        return data

    def getInventory(self, identifier: int) -> list['Product_Package_Inventory']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getInventory', id=identifier)
        from SoftLayer.sltypes.Product_Package_Inventory import Product_Package_Inventory
        return data

    def getIsEngineeredServerProduct(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getIsEngineeredServerProduct', id=identifier)
        return data

    def getItemCategory(self, identifier: int) -> 'Product_Item_Category':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getItemCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getLocalDiskFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getLocalDiskFlag', id=identifier)
        return data

    def getLocationConflicts(self, identifier: int) -> list['Product_Item_Resource_Conflict']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getLocationConflicts', id=identifier)
        from SoftLayer.sltypes.Product_Item_Resource_Conflict import Product_Item_Resource_Conflict
        return data

    def getM2DriveFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getM2DriveFlag', id=identifier)
        return data

    def getMinimumNvmeBays(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getMinimumNvmeBays', id=identifier)
        return data

    def getNvmeDiskFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getNvmeDiskFlag', id=identifier)
        return data

    def getObjectStorageClusterGeolocationType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getObjectStorageClusterGeolocationType', id=identifier)
        return data

    def getObjectStorageItemFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getObjectStorageItemFlag', id=identifier)
        return data

    def getObjectStorageServiceClass(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getObjectStorageServiceClass', id=identifier)
        return data

    def getPackages(self, identifier: int) -> list['Product_Package']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getPackages', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getPcieDriveFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getPcieDriveFlag', id=identifier)
        return data

    def getPhysicalCoreCapacity(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getPhysicalCoreCapacity', id=identifier)
        return data

    def getPresaleEvents(self, identifier: int) -> list['Sales_Presale_Event']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getPresaleEvents', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getPrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getRequirements(self, identifier: int) -> list['Product_Item_Requirement']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getRequirements', id=identifier)
        from SoftLayer.sltypes.Product_Item_Requirement import Product_Item_Requirement
        return data

    def getRules(self, identifier: int) -> list['Product_Item_Rule']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getRules', id=identifier)
        from SoftLayer.sltypes.Product_Item_Rule import Product_Item_Rule
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getTaxCategory(self, identifier: int) -> 'Product_Item_Tax_Category':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getTaxCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Tax_Category import Product_Item_Tax_Category
        return data

    def getThirdPartyPolicyAssignments(self, identifier: int) -> list['Product_Item_Policy_Assignment']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getThirdPartyPolicyAssignments', id=identifier)
        from SoftLayer.sltypes.Product_Item_Policy_Assignment import Product_Item_Policy_Assignment
        return data

    def getThirdPartySupportVendor(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getThirdPartySupportVendor', id=identifier)
        return data

    def getTotalPhysicalCoreCapacity(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getTotalPhysicalCoreCapacity', id=identifier)
        return data

    def getTotalPhysicalCoreCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getTotalPhysicalCoreCount', id=identifier)
        return data

    def getTotalProcessorCapacity(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getTotalProcessorCapacity', id=identifier)
        return data

    def getUpgradeItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getUpgradeItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getUpgradeItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Item', 'getUpgradeItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data
