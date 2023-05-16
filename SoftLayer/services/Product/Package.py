# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Package(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Package'
        self.client = client

    def getActiveItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getActiveItems',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getActivePackagesByAttribute(
        self,
        attributeKeyName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActivePackagesByAttribute',
            attributeKeyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getActivePrivateHostedCloudPackages(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActivePrivateHostedCloudPackages',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getActiveUsageRatePrices(
        self,
        locationId: int,
        categoryCode: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getActiveUsageRatePrices',
            locationId,
            categoryCode,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getAvailablePackagesForImageTemplate(
        self,
        imageTemplate: SoftLayer_Virtual_Guest_Block_Device_Template_Group,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getAvailablePackagesForImageTemplate',
            imageTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getCdnItems(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getCdnItems',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getCloudStorageItems(
        self,
        provider: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getCloudStorageItems',
            provider,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getItemAvailabilityTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Attribute_Type]':

        data = self.client.call(
            self.service,
            'getItemAvailabilityTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Attribute.Type import Type
        return Type(data)


    def getItemPricesFromSoftwareDescriptions(
        self,
        softwareDescriptions: SoftLayer_Software_Description,
        includeTranslationsFlag: boolean,
        returnAllPricesFlag: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getItemPricesFromSoftwareDescriptions',
            softwareDescriptions,
            includeTranslationsFlag,
            returnAllPricesFlag,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getItemsFromImageTemplate(
        self,
        imageTemplate: SoftLayer_Virtual_Guest_Block_Device_Template_Group,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getItemsFromImageTemplate',
            imageTemplate,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getMessageQueueItems(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getMessageQueueItems',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getObjectStorageDatacenters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Container_Product_Order_Network_Storage_Hub_Datacenter]':

        data = self.client.call(
            self.service,
            'getObjectStorageDatacenters',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Container.Product.Order.Network.Storage.Hub.Datacenter import Datacenter
        return Datacenter(data)


    def getObjectStorageLocationGroups(
        self,
        
    ) -> 'list[SoftLayer_Container_Product_Order_Network_Storage_ObjectStorage_LocationGroup]':

        data = self.client.call(
            self.service,
            'getObjectStorageLocationGroups',
            
        )
        from SoftLayer.datatypes.Container.Product.Order.Network.Storage.ObjectStorage.LocationGroup import LocationGroup
        return LocationGroup(data)


    def getStandardCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getStandardCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getAccountRestrictedActivePresets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Preset]':

        data = self.client.call(
            self.service,
            'getAccountRestrictedActivePresets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return Preset(data)


    def getAccountRestrictedCategories(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getAccountRestrictedCategories',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getAccountRestrictedPricesFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAccountRestrictedPricesFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getActivePresets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Preset]':

        data = self.client.call(
            self.service,
            'getActivePresets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return Preset(data)


    def getActiveRamItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getActiveRamItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getActiveServerItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getActiveServerItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getActiveSoftwareItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getActiveSoftwareItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getActiveUsagePrices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getActiveUsagePrices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAdditionalServiceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAdditionalServiceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Attribute import Attribute
        return Attribute(data)


    def getAvailableLocations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Locations]':

        data = self.client.call(
            self.service,
            'getAvailableLocations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Locations import Locations
        return Locations(data)


    def getAvailableStorageUnits(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getAvailableStorageUnits',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCategories(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getCategories',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getConfiguration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Order_Configuration]':

        data = self.client.call(
            self.service,
            'getConfiguration',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Order.Configuration import Configuration
        return Configuration(data)


    def getDefaultBootCategoryCode(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDefaultBootCategoryCode',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDefaultRamItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getDefaultRamItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getDeploymentNodeType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDeploymentNodeType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDeploymentPackages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getDeploymentPackages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getDeploymentType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDeploymentType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDeployments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getDeployments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getDisallowCustomDiskPartitions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDisallowCustomDiskPartitions',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFirstOrderStep(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Order_Step':

        data = self.client.call(
            self.service,
            'getFirstOrderStep',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Order.Step import Step
        return Step(data)


    def getGatewayApplianceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getGatewayApplianceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGpuFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getGpuFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHourlyBillingAvailableFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHourlyBillingAvailableFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHourlyOnlyOrders(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHourlyOnlyOrders',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getItemConflicts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Resource_Conflict]':

        data = self.client.call(
            self.service,
            'getItemConflicts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Resource.Conflict import Conflict
        return Conflict(data)


    def getItemLocationConflicts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Resource_Conflict]':

        data = self.client.call(
            self.service,
            'getItemLocationConflicts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Resource.Conflict import Conflict
        return Conflict(data)


    def getItemPriceReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Item_Prices]':

        data = self.client.call(
            self.service,
            'getItemPriceReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Item.Prices import Prices
        return Prices(data)


    def getItemPrices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getItemPrices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getLocations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getLocations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getLowestServerPrice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getLowestServerPrice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getMaximumPortSpeed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getMaximumPortSpeed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMinimumPortSpeed(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getMinimumPortSpeed',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMongoDbEngineeredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMongoDbEngineeredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNoUpgradesFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNoUpgradesFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNonEuCompliantFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNonEuCompliantFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOrderPremiums(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price_Premium]':

        data = self.client.call(
            self.service,
            'getOrderPremiums',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price.Premium import Premium
        return Premium(data)


    def getPopLocationAvailabilityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPopLocationAvailabilityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPreconfiguredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPreconfiguredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPresetConfigurationRequiredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPresetConfigurationRequiredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPreventVlanSelectionFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPreventVlanSelectionFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrivateHostedCloudPackageFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPrivateHostedCloudPackageFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrivateHostedCloudPackageType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPrivateHostedCloudPackageType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPrivateNetworkOnlyFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPrivateNetworkOnlyFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getQuantaStorPackageFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getQuantaStorPackageFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRaidDiskRestrictionFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getRaidDiskRestrictionFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRedundantPowerFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getRedundantPowerFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getRegions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location_Region]':

        data = self.client.call(
            self.service,
            'getRegions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location.Region import Region
        return Region(data)


    def getTopLevelItemCategoryCode(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getTopLevelItemCategoryCode',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Type import Type
        return Type(data)


