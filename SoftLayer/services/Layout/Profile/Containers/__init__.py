# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Profile_Containers(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Profile_Containers'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Layout_Profile_Containers',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Layout_Profile_Containers':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile.Containers import Containers
        return Containers(data)


    def editObject(
        self,
        templateObject: 'SoftLayer_Layout_Profile_Containers',
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
    ) -> 'SoftLayer_Layout_Profile_Containers':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile.Containers import Containers
        return Containers(data)


    def getLayoutContainerType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Container':

        data = self.client.call(
            self.service,
            'getLayoutContainerType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getLayoutProfile(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Profile':

        data = self.client.call(
            self.service,
            'getLayoutProfile',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile import Profile
        return Profile(data)


