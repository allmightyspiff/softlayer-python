# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand_Restriction_Location_CustomerCountry(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand_Restriction_Location_CustomerCountry'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Restriction_Location_CustomerCountry]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Restriction.Location.CustomerCountry import CustomerCountry
        return CustomerCountry(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand_Restriction_Location_CustomerCountry':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand.Restriction.Location.CustomerCountry import CustomerCountry
        return CustomerCountry(data)


    def getBrand(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getBrand',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


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


