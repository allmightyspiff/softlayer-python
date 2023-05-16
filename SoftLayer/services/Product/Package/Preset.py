# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Package_Preset(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Package_Preset'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Preset]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return Preset(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Preset':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return Preset(data)


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


    def getBareMetalReservedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBareMetalReservedFlag',
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


    def getComputeGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Server_Group':

        data = self.client.call(
            self.service,
            'getComputeGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Server.Group import Group
        return Group(data)


    def getConfiguration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Preset_Configuration]':

        data = self.client.call(
            self.service,
            'getConfiguration',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Preset.Configuration import Configuration
        return Configuration(data)


    def getDisallowedComputeGroupUpgradeFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDisallowedComputeGroupUpgradeFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFixedConfigurationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getFixedConfigurationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


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


    def getLowestPresetServerPrice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getLowestPresetServerPrice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getPackage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package':

        data = self.client.call(
            self.service,
            'getPackage',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getPackageConfiguration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Order_Configuration]':

        data = self.client.call(
            self.service,
            'getPackageConfiguration',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Order.Configuration import Configuration
        return Configuration(data)


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


    def getStorageGroupTemplateArrays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group_Template_Group]':

        data = self.client.call(
            self.service,
            'getStorageGroupTemplateArrays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Group.Template.Group import Group
        return Group(data)


    def getTotalMinimumHourlyFee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getTotalMinimumHourlyFee',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTotalMinimumRecurringFee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getTotalMinimumRecurringFee',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


