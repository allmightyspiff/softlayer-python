# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Container(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Container'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Layout_Container]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Container':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getLayoutContainerType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Container_Type':

        data = self.client.call(
            self.service,
            'getLayoutContainerType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Container.Type import Type
        return Type(data)


    def getLayoutItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Item]':

        data = self.client.call(
            self.service,
            'getLayoutItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Item import Item
        return Item(data)


