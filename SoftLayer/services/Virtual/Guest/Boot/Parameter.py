# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Virtual_Guest_Boot_Parameter(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Virtual_Guest_Boot_Parameter'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Virtual_Guest_Boot_Parameter
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
        templateObject: SoftLayer_Virtual_Guest_Boot_Parameter
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Boot_Parameter':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Boot.Parameter import Parameter
        return Parameter(data)


    def getGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getGuestBootParameterType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest_Boot_Parameter_Type':

        data = self.client.call(
            self.service,
            'getGuestBootParameterType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest.Boot.Parameter.Type import Type
        return Type(data)


