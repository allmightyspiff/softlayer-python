from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Package(Entity):
    """The SoftLayer_Product_Package data type contains information about packages from which orders can be
generated. Packages contain general information regarding what is in them, where they are currently sold,
availability, and pricing."""
    description: str
    firstOrderStepId: int
    id_: int
    isActive: int
    keyName: str
    name: str
    subDescription: str
    unitSize: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Package'

    def getActiveItems(self, identifier: int) -> list['Product_Item']:
        """Retrieve the active items, as well as their prices and categories for this package"""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getActivePackagesByAttribute(self, attributeKeyName: str) -> list['Product_Package']:
        """[<strong>DEPRECATED</strong>] Retrieve the active [[SoftLayer_Product_Package]] objects from which you can
order a server, service or software filtered by an attribute type
([[SoftLayer_Product_Package_Attribute_Type]]) on the package."""
        data = self.client.call('SoftLayer_Product_Package', 'getActivePackagesByAttribute', attributeKeyName)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getActivePrivateHostedCloudPackages(self) -> list['Product_Package']:
        """[DEPRECATED] Get the Active SoftLayer_Product_Packages from which one can order private hosted cloud
configurations."""
        data = self.client.call('SoftLayer_Product_Package', 'getActivePrivateHostedCloudPackages')
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getActiveUsageRatePrices(self, identifier: int, locationId: int, categoryCode: str) -> list['Product_Item_Price']:
        """Return the active usage rate prices for the current package."""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveUsageRatePrices', locationId, categoryCode, id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAllObjects(self) -> list['Product_Package']:
        """Get the Active SoftLayer_Product_Packages"""
        data = self.client.call('SoftLayer_Product_Package', 'getAllObjects')
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getAvailablePackagesForImageTemplate(self, imageTemplate: 'Virtual_Guest_Block_Device_Template_Group') -> list['Product_Package']:
        data = self.client.call('SoftLayer_Product_Package', 'getAvailablePackagesForImageTemplate', imageTemplate)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getCdnItems(self, identifier: int) -> list['Product_Item']:
        data = self.client.call('SoftLayer_Product_Package', 'getCdnItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getCloudStorageItems(self, identifier: int, provider: int) -> list['Product_Item']:
        data = self.client.call('SoftLayer_Product_Package', 'getCloudStorageItems', provider, id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getItemAvailabilityTypes(self) -> list['Product_Item_Attribute_Type']:
        """Returns a collection of SoftLayer_Product_Item_Attribute_Type objects."""
        data = self.client.call('SoftLayer_Product_Package', 'getItemAvailabilityTypes')
        from SoftLayer.sltypes.Product_Item_Attribute_Type import Product_Item_Attribute_Type
        return data

    def getItemPricesFromSoftwareDescriptions(self, identifier: int, softwareDescriptions: 'Software_Description', includeTranslationsFlag: bool, returnAllPricesFlag: bool) -> list['Product_Item_Price']:
        """Returns a collection of SoftLayer_Item_Price objects from a collection of SoftLayer_Software_Description that
are available for the service offering (package)."""
        data = self.client.call('SoftLayer_Product_Package', 'getItemPricesFromSoftwareDescriptions', softwareDescriptions, includeTranslationsFlag, returnAllPricesFlag, id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getItemsFromImageTemplate(self, identifier: int, imageTemplate: 'Virtual_Guest_Block_Device_Template_Group') -> list['Product_Item']:
        """Return a collection of [[SoftLayer_Product_Item]] objects from a
[[SoftLayer_Virtual_Guest_Block_Device_Template_Group]] object"""
        data = self.client.call('SoftLayer_Product_Package', 'getItemsFromImageTemplate', imageTemplate, id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getMessageQueueItems(self, identifier: int) -> list['Product_Item']:
        data = self.client.call('SoftLayer_Product_Package', 'getMessageQueueItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getObject(self, identifier: int) -> 'Product_Package':
        """Retrieve a SoftLayer_Product_Package record."""
        data = self.client.call('SoftLayer_Product_Package', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getObjectStorageDatacenters(self, identifier: int) -> list['Container_Product_Order_Network_Storage_Hub_Datacenter']:
        """Returns a collection of datacenters where object storage is available plus the associated active usage rate
prices."""
        data = self.client.call('SoftLayer_Product_Package', 'getObjectStorageDatacenters', id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Network_Storage_Hub_Datacenter import Container_Product_Order_Network_Storage_Hub_Datacenter
        return data

    def getObjectStorageLocationGroups(self, identifier: int) -> list['Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup']:
        """Returns a collection of location groups where object storage is available plus the associated active usage
rate prices."""
        data = self.client.call('SoftLayer_Product_Package', 'getObjectStorageLocationGroups', id=identifier)
        from SoftLayer.sltypes.Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup import Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup
        return data

    def getStandardCategories(self, identifier: int) -> list['Product_Item_Category']:
        """This call is similar to [[SoftLayer_Product_Package/getCategories|getCategories]], except that it does not
include account-restricted pricing. Not all accounts have restricted pricing."""
        data = self.client.call('SoftLayer_Product_Package', 'getStandardCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getAccountRestrictedActivePresets(self, identifier: int) -> list['Product_Package_Preset']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAccountRestrictedActivePresets', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getAccountRestrictedCategories(self, identifier: int) -> list['Product_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAccountRestrictedCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getAccountRestrictedPricesFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAccountRestrictedPricesFlag', id=identifier)
        return data

    def getActivePresets(self, identifier: int) -> list['Product_Package_Preset']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getActivePresets', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getActiveRamItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveRamItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getActiveServerItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveServerItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getActiveSoftwareItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveSoftwareItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getActiveUsagePrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getActiveUsagePrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getAdditionalServiceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAdditionalServiceFlag', id=identifier)
        return data

    def getAttributes(self, identifier: int) -> list['Product_Package_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Product_Package_Attribute import Product_Package_Attribute
        return data

    def getAvailableLocations(self, identifier: int) -> list['Product_Package_Locations']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAvailableLocations', id=identifier)
        from SoftLayer.sltypes.Product_Package_Locations import Product_Package_Locations
        return data

    def getAvailableStorageUnits(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getAvailableStorageUnits', id=identifier)
        return data

    def getCategories(self, identifier: int) -> list['Product_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getConfiguration(self, identifier: int) -> list['Product_Package_Order_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getConfiguration', id=identifier)
        from SoftLayer.sltypes.Product_Package_Order_Configuration import Product_Package_Order_Configuration
        return data

    def getDefaultBootCategoryCode(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDefaultBootCategoryCode', id=identifier)
        return data

    def getDefaultRamItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDefaultRamItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getDeploymentNodeType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDeploymentNodeType', id=identifier)
        return data

    def getDeploymentPackages(self, identifier: int) -> list['Product_Package']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDeploymentPackages', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getDeploymentType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDeploymentType', id=identifier)
        return data

    def getDeployments(self, identifier: int) -> list['Product_Package']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDeployments', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getDisallowCustomDiskPartitions(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getDisallowCustomDiskPartitions', id=identifier)
        return data

    def getFirstOrderStep(self, identifier: int) -> 'Product_Package_Order_Step':
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getFirstOrderStep', id=identifier)
        from SoftLayer.sltypes.Product_Package_Order_Step import Product_Package_Order_Step
        return data

    def getGatewayApplianceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getGatewayApplianceFlag', id=identifier)
        return data

    def getGpuFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getGpuFlag', id=identifier)
        return data

    def getHourlyBillingAvailableFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getHourlyBillingAvailableFlag', id=identifier)
        return data

    def getHourlyOnlyOrders(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getHourlyOnlyOrders', id=identifier)
        return data

    def getItemConflicts(self, identifier: int) -> list['Product_Item_Resource_Conflict']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getItemConflicts', id=identifier)
        from SoftLayer.sltypes.Product_Item_Resource_Conflict import Product_Item_Resource_Conflict
        return data

    def getItemLocationConflicts(self, identifier: int) -> list['Product_Item_Resource_Conflict']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getItemLocationConflicts', id=identifier)
        from SoftLayer.sltypes.Product_Item_Resource_Conflict import Product_Item_Resource_Conflict
        return data

    def getItemPriceReferences(self, identifier: int) -> list['Product_Package_Item_Prices']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getItemPriceReferences', id=identifier)
        from SoftLayer.sltypes.Product_Package_Item_Prices import Product_Package_Item_Prices
        return data

    def getItemPrices(self, identifier: int) -> list['Product_Item_Price']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getItemPrices', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getLocations(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getLocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getLowestServerPrice(self, identifier: int) -> 'Product_Item_Price':
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getLowestServerPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getMaximumPortSpeed(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getMaximumPortSpeed', id=identifier)
        return data

    def getMinimumPortSpeed(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getMinimumPortSpeed', id=identifier)
        return data

    def getMongoDbEngineeredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getMongoDbEngineeredFlag', id=identifier)
        return data

    def getNoUpgradesFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getNoUpgradesFlag', id=identifier)
        return data

    def getNonEuCompliantFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getNonEuCompliantFlag', id=identifier)
        return data

    def getOrderPremiums(self, identifier: int) -> list['Product_Item_Price_Premium']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getOrderPremiums', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Premium import Product_Item_Price_Premium
        return data

    def getPopLocationAvailabilityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPopLocationAvailabilityFlag', id=identifier)
        return data

    def getPreconfiguredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPreconfiguredFlag', id=identifier)
        return data

    def getPresetConfigurationRequiredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPresetConfigurationRequiredFlag', id=identifier)
        return data

    def getPreventVlanSelectionFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPreventVlanSelectionFlag', id=identifier)
        return data

    def getPrivateHostedCloudPackageFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPrivateHostedCloudPackageFlag', id=identifier)
        return data

    def getPrivateHostedCloudPackageType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPrivateHostedCloudPackageType', id=identifier)
        return data

    def getPrivateNetworkOnlyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getPrivateNetworkOnlyFlag', id=identifier)
        return data

    def getQuantaStorPackageFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getQuantaStorPackageFlag', id=identifier)
        return data

    def getRaidDiskRestrictionFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getRaidDiskRestrictionFlag', id=identifier)
        return data

    def getRedundantPowerFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getRedundantPowerFlag', id=identifier)
        return data

    def getRegions(self, identifier: int) -> list['Location_Region']:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getRegions', id=identifier)
        from SoftLayer.sltypes.Location_Region import Location_Region
        return data

    def getTopLevelItemCategoryCode(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getTopLevelItemCategoryCode', id=identifier)
        return data

    def getType(self, identifier: int) -> 'Product_Package_Type':
        """"""
        data = self.client.call('SoftLayer_Product_Package', 'getType', id=identifier)
        from SoftLayer.sltypes.Product_Package_Type import Product_Package_Type
        return data
