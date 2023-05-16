# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Layout_Profile_Customer(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Layout_Profile_Customer'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Layout_Profile_Customer':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Layout.Profile.Customer import Customer
        return Customer(data)


    def createObject(
        self,
        templateObject: SoftLayer_Layout_Profile
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject
        )
        
        return data


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Layout_Profile
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def modifyPreference(
        self,
        templateObject: SoftLayer_Layout_Profile_Preference,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Layout_Profile_Preference':

        data = self.client.call(
            self.service,
            'modifyPreference',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


    def modifyPreferences(
        self,
        layoutPreferenceObjects: SoftLayer_Layout_Profile_Preference,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Layout_Profile_Preference]':

        data = self.client.call(
            self.service,
            'modifyPreferences',
            layoutPreferenceObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


    def getUserRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUserRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getLayoutContainers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Container]':

        data = self.client.call(
            self.service,
            'getLayoutContainers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Container import Container
        return Container(data)


    def getLayoutPreferences(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Layout_Profile_Preference]':

        data = self.client.call(
            self.service,
            'getLayoutPreferences',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Layout.Profile.Preference import Preference
        return Preference(data)


