# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Profile(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Profile'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Layout_Profile'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data


    def deleteObject(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Layout_Profile',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Profile':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


    def modifyPreference(
        self,
        templateObject: 'SoftLayer_Layout_Profile_Preference',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Layout_Profile_Preference':

        data = self.client.call(
            self.service,
            'modifyPreference',
            templateObject,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


    def modifyPreferences(
        self,
        layoutPreferenceObjects: 'SoftLayer_Layout_Profile_Preference',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile_Preference]':

        data = self.client.call(
            self.service,
            'modifyPreferences',
            layoutPreferenceObjects,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


    def getLayoutContainers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Container]':

        data = self.client.call(
            self.service,
            'getLayoutContainers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getLayoutPreferences(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Profile_Preference]':

        data = self.client.call(
            self.service,
            'getLayoutPreferences',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


