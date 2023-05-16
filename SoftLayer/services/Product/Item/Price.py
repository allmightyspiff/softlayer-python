# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Price(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Price'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getUsageRatePrices(
        self,
        location: SoftLayer_Location,
        items: SoftLayer_Product_Item,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUsageRatePrices',
            location,
            items,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getAccountRestrictions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price_Account_Restriction]':

        data = self.client.call(
            self.service,
            'getAccountRestrictions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price.Account.Restriction import Restriction
        return Restriction(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price.Attribute import Attribute
        return Attribute(data)


    def getBareMetalReservedCapacityFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBareMetalReservedCapacityFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBigDataOsJournalDiskFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBigDataOsJournalDiskFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBundleReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Bundles]':

        data = self.client.call(
            self.service,
            'getBundleReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Bundles import Bundles
        return Bundles(data)


    def getCapacityRestrictionMaximum(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacityRestrictionMaximum',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCapacityRestrictionMinimum(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacityRestrictionMinimum',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCapacityRestrictionType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getCapacityRestrictionType',
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


    def getDedicatedHostInstanceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDedicatedHostInstanceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDefinedSoftwareLicenseFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDefinedSoftwareLicenseFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEligibilityStrategy(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getEligibilityStrategy',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item':

        data = self.client.call(
            self.service,
            'getItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


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


    def getPackageReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Item_Prices]':

        data = self.client.call(
            self.service,
            'getPackageReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Item.Prices import Prices
        return Prices(data)


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


    def getPresetConfigurations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Preset_Configuration]':

        data = self.client.call(
            self.service,
            'getPresetConfigurations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Preset.Configuration import Configuration
        return Configuration(data)


    def getPriceType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPriceType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPricingLocationGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Pricing':

        data = self.client.call(
            self.service,
            'getPricingLocationGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Pricing import Pricing
        return Pricing(data)


    def getRequiredCoreCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getRequiredCoreCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReservedCapacityInstanceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getReservedCapacityInstanceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


