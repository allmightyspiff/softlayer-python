# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Item(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Item'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Item':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Item import Item
        return Item(data)


    def getLayoutItemPreferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Preference]':

        data = self.client.call(
            self.service,
            'getLayoutItemPreferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Preference import Preference
        return Preference(data)


    def getLayoutItemType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Item_Type':

        data = self.client.call(
            self.service,
            'getLayoutItemType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Item.Type import Type
        return Type(data)


