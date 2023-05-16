# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Backbone(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Backbone'
        self.client = client

    def getAllBackbones(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Backbone]':

        data = self.client.call(
            self.service,
            'getAllBackbones',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return Backbone(data)


    def getBackbonesForLocationName(
        self,
        locationName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Backbone]':

        data = self.client.call(
            self.service,
            'getBackbonesForLocationName',
            locationName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return Backbone(data)


    def getGraphImage(
        self,
        identifier: int
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getGraphImage',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Backbone':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return Backbone(data)


    def getHealth(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getHealth',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLocation(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getNetworkComponent(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':

        data = self.client.call(
            self.service,
            'getNetworkComponent',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return Component(data)


