# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Category(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Category'
        self.client = client

    def getAdditionalProductsForCategory(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getAdditionalProductsForCategory',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getBandwidthCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getBandwidthCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getComputingCategories(
        self,
        resetCache: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getComputingCategories',
            resetCache,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getCustomUsageRatesCategories(
        self,
        resetCache: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getCustomUsageRatesCategories',
            resetCache,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getExternalResourceCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getExternalResourceCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Category':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getObjectStorageCategories(
        self,
        resetCache: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getObjectStorageCategories',
            resetCache,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getSoftwareCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getSoftwareCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getSubnetCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getSubnetCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getTopLevelCategories(
        self,
        resetCache: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getTopLevelCategories',
            resetCache,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getValidCancelableServiceItemCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getValidCancelableServiceItemCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getVlanCategories(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Category]':

        data = self.client.call(
            self.service,
            'getVlanCategories',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Category import Category
        return Category(data)


    def getBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Category_Group':

        data = self.client.call(
            self.service,
            'getGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Item.Category.Group import Group
        return Group(data)


    def getGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Item_Category_Group]':

        data = self.client.call(
            self.service,
            'getGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Item.Category.Group import Group
        return Group(data)


    def getOrderOptions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Category_Order_Option_Type]':

        data = self.client.call(
            self.service,
            'getOrderOptions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Category.Order.Option.Type import Type
        return Type(data)


    def getPackageConfigurations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Order_Configuration]':

        data = self.client.call(
            self.service,
            'getPackageConfigurations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Order.Configuration import Configuration
        return Configuration(data)


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


    def getQuestionReferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Category_Question_Xref]':

        data = self.client.call(
            self.service,
            'getQuestionReferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Category.Question.Xref import Xref
        return Xref(data)


    def getQuestions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Category_Question]':

        data = self.client.call(
            self.service,
            'getQuestions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Category.Question import Question
        return Question(data)


