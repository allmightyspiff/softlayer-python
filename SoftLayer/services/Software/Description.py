# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Software_Description(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Software_Description'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Software_Description]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getCustomerOwnedLicenseDescriptions(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Software_Description]':

        data = self.client.call(
            self.service,
            'getCustomerOwnedLicenseDescriptions',
            mask=objectMask
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Description_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Description.Attribute import Attribute
        return Attribute(data)


    def getAverageInstallationDuration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getAverageInstallationDuration',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCompatibleSoftwareDescriptions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Description]':

        data = self.client.call(
            self.service,
            'getCompatibleSoftwareDescriptions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getFeatures(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Description_Feature]':

        data = self.client.call(
            self.service,
            'getFeatures',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Description.Feature import Feature
        return Feature(data)


    def getLatestVersion(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Description]':

        data = self.client.call(
            self.service,
            'getLatestVersion',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getProductItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item]':

        data = self.client.call(
            self.service,
            'getProductItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item import Item
        return Item(data)


    def getProvisionTransactionGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction_Group':

        data = self.client.call(
            self.service,
            'getProvisionTransactionGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.Group import Group
        return Group(data)


    def getReloadTransactionGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction_Group':

        data = self.client.call(
            self.service,
            'getReloadTransactionGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.Group import Group
        return Group(data)


    def getRequiredUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getRequiredUser',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSoftwareLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_License]':

        data = self.client.call(
            self.service,
            'getSoftwareLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.License import License
        return License(data)


    def getUpgradeSoftwareDescription(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getUpgradeSoftwareDescription',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getUpgradeSwDesc(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getUpgradeSwDesc',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getValidFilesystemTypes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Filesystem_Type]':

        data = self.client.call(
            self.service,
            'getValidFilesystemTypes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Filesystem.Type import Type
        return Type(data)


