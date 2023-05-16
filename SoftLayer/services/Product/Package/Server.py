# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Product_Package_Server(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Product_Package_Server'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Package_Server]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Package.Server import Server
        return Server(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Server':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Server import Server
        return Server(data)


    def getCatalog(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Catalog':

        data = self.client.call(
            self.service,
            'getCatalog',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Catalog import Catalog
        return Catalog(data)


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


    def getItemPrice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Item_Price':

        data = self.client.call(
            self.service,
            'getItemPrice',
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


    def getPreset(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Package_Preset':

        data = self.client.call(
            self.service,
            'getPreset',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Package.Preset import Preset
        return Preset(data)


