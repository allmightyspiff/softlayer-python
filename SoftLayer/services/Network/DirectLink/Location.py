# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_DirectLink_Location(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_DirectLink_Location'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_DirectLink_Location]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.DirectLink.Location import Location
        return Location(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_Location':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.Location import Location
        return Location(data)


    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':

        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_Provider':

        data = self.client.call(
            self.service,
            'getProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.Provider import Provider
        return Provider(data)


    def getServiceType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_ServiceType':

        data = self.client.call(
            self.service,
            'getServiceType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.ServiceType import ServiceType
        return ServiceType(data)


