# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Profile_Preference(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Profile_Preference'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Profile_Preference':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


    def getLayoutContainer(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Container':

        data = self.client.call(
            self.service,
            'getLayoutContainer',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getLayoutItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Item':

        data = self.client.call(
            self.service,
            'getLayoutItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Item import Item
        return Item(data)


    def getLayoutPreference(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Preference':

        data = self.client.call(
            self.service,
            'getLayoutPreference',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Preference import Preference
        return Preference(data)


    def getLayoutProfile(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Profile':

        data = self.client.call(
            self.service,
            'getLayoutProfile',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


