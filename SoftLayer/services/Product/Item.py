# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getActivePresaleEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Sales_Presale_Event]':

        data = self.client.call(
            self.service,
            'getActivePresaleEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


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


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Attribute import Attribute
        return Attribute(data)


    def getAvailabilityAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Attribute]':

        data = self.client.call(
            self.service,
            'getAvailabilityAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Attribute import Attribute
        return Attribute(data)


    def getBillingType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBillingType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBundle(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Bundles]':

        data = self.client.call(
            self.service,
            'getBundle',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Bundles import Bundles
        return Bundles(data)


    def getBundleItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getBundleItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getCapacityMaximum(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacityMaximum',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCapacityMinimum(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacityMinimum',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCapacityRestrictedProductFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCapacityRestrictedProductFlag',
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


    def getConfigurationTemplates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Template]':

        data = self.client.call(
            self.service,
            'getConfigurationTemplates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Template import Template
        return Template(data)


    def getConflicts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Resource_Conflict]':

        data = self.client.call(
            self.service,
            'getConflicts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Resource.Conflict import Conflict
        return Conflict(data)


    def getCoreRestrictedItemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCoreRestrictedItemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDowngradeItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getDowngradeItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getDowngradeItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getDowngradeItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getGlobalCategoryConflicts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Resource_Conflict]':

        data = self.client.call(
            self.service,
            'getGlobalCategoryConflicts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Resource.Conflict import Conflict
        return Conflict(data)


    def getHardwareGenericComponentModel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Model_Generic':

        data = self.client.call(
            self.service,
            'getHardwareGenericComponentModel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Generic import Generic
        return Generic(data)


    def getHideFromPortalFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHideFromPortalFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIneligibleForAccountDiscountFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIneligibleForAccountDiscountFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInventory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Inventory]':

        data = self.client.call(
            self.service,
            'getInventory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Inventory import Inventory
        return Inventory(data)


    def getIsEngineeredServerProduct(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsEngineeredServerProduct',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getItemCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Category':

        data = self.client.call(
            self.service,
            'getItemCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getLocalDiskFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getLocalDiskFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLocationConflicts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Resource_Conflict]':

        data = self.client.call(
            self.service,
            'getLocationConflicts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Resource.Conflict import Conflict
        return Conflict(data)


    def getM2DriveFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getM2DriveFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMinimumNvmeBays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getMinimumNvmeBays',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNvmeDiskFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNvmeDiskFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getObjectStorageClusterGeolocationType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getObjectStorageClusterGeolocationType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getObjectStorageItemFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getObjectStorageItemFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getObjectStorageServiceClass(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getObjectStorageServiceClass',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPackages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getPackages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getPcieDriveFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPcieDriveFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPhysicalCoreCapacity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPhysicalCoreCapacity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPresaleEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Sales_Presale_Event]':

        data = self.client.call(
            self.service,
            'getPresaleEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


    def getPrices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getPrices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getRequirements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Requirement]':

        data = self.client.call(
            self.service,
            'getRequirements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Requirement import Requirement
        return Requirement(data)


    def getRules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Rule]':

        data = self.client.call(
            self.service,
            'getRules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Rule import Rule
        return Rule(data)


    def getSoftwareDescription(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getSoftwareDescription',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getTaxCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Tax_Category':

        data = self.client.call(
            self.service,
            'getTaxCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Tax.Category import Category
        return Category(data)


    def getThirdPartyPolicyAssignments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Policy_Assignment]':

        data = self.client.call(
            self.service,
            'getThirdPartyPolicyAssignments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Policy.Assignment import Assignment
        return Assignment(data)


    def getThirdPartySupportVendor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getThirdPartySupportVendor',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalPhysicalCoreCapacity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getTotalPhysicalCoreCapacity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalPhysicalCoreCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getTotalPhysicalCoreCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalProcessorCapacity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getTotalProcessorCapacity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getUpgradeItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getUpgradeItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getUpgradeItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getUpgradeItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


