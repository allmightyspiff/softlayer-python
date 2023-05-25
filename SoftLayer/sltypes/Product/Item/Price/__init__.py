from SoftLayer.sltypes.Product.Item.Category.Order.Option.Type import Product_Item_Category_Order_Option_Type
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item_Price(Entity):
    """The SoftLayer_Product_Item_Price data type contains general information relating to a single SoftLayer
product item price. You can find out what packages each price is in as well as which category under which
this price is sold. All prices are returned in floating point values measured in US Dollars ($USD)."""
    currentPriceFlag: bool
    hourlyRecurringFee: float
    id_: int
    itemId: int
    laborFee: float
    locationGroupId: int
    onSaleFlag: bool
    oneTimeFee: float
    oneTimeFeeTax: float
    orderOptions: list[Product_Item_Category_Order_Option_Type]
    proratedRecurringFee: float
    proratedRecurringFeeTax: float
    quantity: int
    recurringFee: float
    recurringFeeTax: float
    setupFee: float
    sort: int
    termLength: int
    tierMinimumThreshold: int
    usageRate: float

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item_Price'

    def getObject(self, identifier: int) -> 'Product_Item_Price':
        """Retrieve a SoftLayer_Product_Item_Price record."""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getObject', id=identifier)
        return data

    def getUsageRatePrices(self, location: 'Location', items: 'Product_Item') -> list['Product_Item_Price']:
        """Get all the rate-based prices for the location and items specified."""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getUsageRatePrices', location, items)
        return data

    def getAccountRestrictions(self, identifier: int) -> list['Product_Item_Price_Account_Restriction']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getAccountRestrictions', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Account_Restriction import Product_Item_Price_Account_Restriction
        return data

    def getAttributes(self, identifier: int) -> list['Product_Item_Price_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Attribute import Product_Item_Price_Attribute
        return data

    def getBareMetalReservedCapacityFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getBareMetalReservedCapacityFlag', id=identifier)
        return data

    def getBigDataOsJournalDiskFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getBigDataOsJournalDiskFlag', id=identifier)
        return data

    def getBundleReferences(self, identifier: int) -> list['Product_Item_Bundles']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getBundleReferences', id=identifier)
        from SoftLayer.sltypes.Product_Item_Bundles import Product_Item_Bundles
        return data

    def getCapacityRestrictionMaximum(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getCapacityRestrictionMaximum', id=identifier)
        return data

    def getCapacityRestrictionMinimum(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getCapacityRestrictionMinimum', id=identifier)
        return data

    def getCapacityRestrictionType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getCapacityRestrictionType', id=identifier)
        return data

    def getCategories(self, identifier: int) -> list['Product_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getCategories', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getDedicatedHostInstanceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getDedicatedHostInstanceFlag', id=identifier)
        return data

    def getDefinedSoftwareLicenseFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getDefinedSoftwareLicenseFlag', id=identifier)
        return data

    def getEligibilityStrategy(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getEligibilityStrategy', id=identifier)
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getOrderPremiums(self, identifier: int) -> list['Product_Item_Price_Premium']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getOrderPremiums', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Premium import Product_Item_Price_Premium
        return data

    def getPackageReferences(self, identifier: int) -> list['Product_Package_Item_Prices']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getPackageReferences', id=identifier)
        from SoftLayer.sltypes.Product_Package_Item_Prices import Product_Package_Item_Prices
        return data

    def getPackages(self, identifier: int) -> list['Product_Package']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getPackages', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getPresetConfigurations(self, identifier: int) -> list['Product_Package_Preset_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getPresetConfigurations', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset_Configuration import Product_Package_Preset_Configuration
        return data

    def getPriceType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getPriceType', id=identifier)
        return data

    def getPricingLocationGroup(self, identifier: int) -> 'Location_Group_Pricing':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getPricingLocationGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group_Pricing import Location_Group_Pricing
        return data

    def getRequiredCoreCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getRequiredCoreCount', id=identifier)
        return data

    def getReservedCapacityInstanceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Price', 'getReservedCapacityInstanceFlag', id=identifier)
        return data
