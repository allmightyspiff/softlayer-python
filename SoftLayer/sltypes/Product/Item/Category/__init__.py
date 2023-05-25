from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Product_Item_Category(Entity):
    """The SoftLayer_Product_Item_Category data type contains general category information for prices."""
    categoryCode: str
    id_: int
    name: str
    quantityLimit: int
    sortOrder: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Product_Item_Category'

    def getAdditionalProductsForCategory(self, identifier: int) -> list['Product_Item']:
        """Return a list of Items in the "Additional Services" package with their active prices for a given product item
category."""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getAdditionalProductsForCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getBandwidthCategories(self) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getBandwidthCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getComputingCategories(self, resetCache: bool) -> list['Product_Item_Category']:
        """Returns a collection of computing categories."""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getComputingCategories', resetCache)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getCustomUsageRatesCategories(self, resetCache: bool) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getCustomUsageRatesCategories', resetCache)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getExternalResourceCategories(self) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getExternalResourceCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getObject(self, identifier: int) -> 'Product_Item_Category':
        """Retrieve a SoftLayer_Product_Item_Category record."""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getObject', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getObjectStorageCategories(self, resetCache: bool) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getObjectStorageCategories', resetCache)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getSoftwareCategories(self) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getSoftwareCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getSubnetCategories(self) -> list['Product_Item_Category']:
        """Returns a list of subnet categories."""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getSubnetCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getTopLevelCategories(self, resetCache: bool) -> list['Product_Item_Category']:
        """Returns a collection of top-level categories."""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getTopLevelCategories', resetCache)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getValidCancelableServiceItemCategories(self) -> list['Product_Item_Category']:
        """Returns service product categories that can be canceled via API"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getValidCancelableServiceItemCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getVlanCategories(self) -> list['Product_Item_Category']:
        data = self.client.call('SoftLayer_Product_Item_Category', 'getVlanCategories')
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getGroup(self, identifier: int) -> 'Product_Item_Category_Group':
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getGroup', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category_Group import Product_Item_Category_Group
        return data

    def getGroups(self, identifier: int) -> list['Product_Package_Item_Category_Group']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getGroups', id=identifier)
        from SoftLayer.sltypes.Product_Package_Item_Category_Group import Product_Package_Item_Category_Group
        return data

    def getOrderOptions(self, identifier: int) -> list['Product_Item_Category_Order_Option_Type']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getOrderOptions', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category_Order_Option_Type import Product_Item_Category_Order_Option_Type
        return data

    def getPackageConfigurations(self, identifier: int) -> list['Product_Package_Order_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getPackageConfigurations', id=identifier)
        from SoftLayer.sltypes.Product_Package_Order_Configuration import Product_Package_Order_Configuration
        return data

    def getPresetConfigurations(self, identifier: int) -> list['Product_Package_Preset_Configuration']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getPresetConfigurations', id=identifier)
        from SoftLayer.sltypes.Product_Package_Preset_Configuration import Product_Package_Preset_Configuration
        return data

    def getQuestionReferences(self, identifier: int) -> list['Product_Item_Category_Question_Xref']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getQuestionReferences', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category_Question_Xref import Product_Item_Category_Question_Xref
        return data

    def getQuestions(self, identifier: int) -> list['Product_Item_Category_Question']:
        """"""
        data = self.client.call('SoftLayer_Product_Item_Category', 'getQuestions', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category_Question import Product_Item_Category_Question
        return data
