# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Item_Category(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Item_Category'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Configuration(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Configuration(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Xref(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Question(data)


