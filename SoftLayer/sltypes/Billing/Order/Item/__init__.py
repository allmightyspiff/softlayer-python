from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Order_Item(Entity):
    """Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data
type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and
port upgrade charges. SoftLayer [[SoftLayer_Billing_Invoice|invoices]] are generated from the cost of a
customer's billing items. Billing items are copied from the product catalog as they're ordered by customers
to create a reference between an account and the billable items they own.   Billing items exist in a tree
relationship. Items are associated with each other by parent/child relationships. Component items such as
CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with.
Billing Items with a null parent item do not have an associated parent item."""
    categoryCode: str
    description: str
    domainName: str
    hostName: str
    hourlyRecurringFee: float
    id_: int
    itemId: int
    itemPriceId: float
    laborAfterTaxAmount: float
    laborFee: float
    laborFeeTaxRate: float
    laborTaxAmount: float
    oneTimeAfterTaxAmount: float
    oneTimeFee: float
    oneTimeFeeTaxRate: float
    oneTimeTaxAmount: float
    parentId: int
    presetId: int
    promoCodeId: int
    quantity: int
    recurringAfterTaxAmount: float
    recurringFee: float
    recurringTaxAmount: float
    setupAfterTaxAmount: float
    setupFee: float
    setupFeeDeferralMonths: int
    setupFeeTaxRate: float
    setupTaxAmount: float

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Order_Item'

    def getObject(self, identifier: int) -> 'Billing_Order_Item':
        """Retrieve a SoftLayer_Billing_Order_Item record."""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getBundledItems(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getBundledItems', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getCategory(self, identifier: int) -> 'Product_Item_Category':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getChildren(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getChildren', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getGlobalIdentifier(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getGlobalIdentifier', id=identifier)
        return data

    def getHardwareGenericComponent(self, identifier: int) -> 'Hardware_Component_Model_Generic':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getHardwareGenericComponent', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Generic import Hardware_Component_Model_Generic
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getItemCategoryAnswers(self, identifier: int) -> list['Billing_Order_Item_Category_Answer']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getItemCategoryAnswers', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item_Category_Answer import Billing_Order_Item_Category_Answer
        return data

    def getItemPrice(self, identifier: int) -> 'Product_Item_Price':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getItemPrice', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price import Product_Item_Price
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getNextOrderChildren(self, identifier: int) -> list['Billing_Order_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getNextOrderChildren', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getOldBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getOldBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getOrder(self, identifier: int) -> 'Billing_Order':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getOrder', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getOrderApprovalDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getOrderApprovalDate', id=identifier)
        return data

    def getPackage(self, identifier: int) -> 'Product_Package':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getPackage', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getParent(self, identifier: int) -> 'Billing_Order_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getParent', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getPreset(self, identifier: int) -> 'Product_Package_Preset':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getPreset', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset import Product_Package_Preset
        return data

    def getPromoCode(self, identifier: int) -> 'Product_Promotion':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getPromoCode', id=identifier)
        from SoftLayer.sltypes.Product_Promotion import Product_Promotion
        return data

    def getRedundantPowerSupplyCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getRedundantPowerSupplyCount', id=identifier)
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getStorageGroups(self, identifier: int) -> list['Configuration_Storage_Group_Order']:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getStorageGroups', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group_Order import Configuration_Storage_Group_Order
        return data

    def getTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getTotalRecurringAmount', id=identifier)
        return data

    def getUpgradeItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Order_Item', 'getUpgradeItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data
