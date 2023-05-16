# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand_Business_Partner(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand_Business_Partner'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand_Business_Partner':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand.Business.Partner import Partner
        return Partner(data)


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


    def getChannel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Channel':

        data = self.client.call(
            self.service,
            'getChannel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Channel import Channel
        return Channel(data)


    def getSegment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Segment':

        data = self.client.call(
            self.service,
            'getSegment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Segment import Segment
        return Segment(data)


