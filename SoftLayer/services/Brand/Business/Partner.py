# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand_Business_Partner(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand_Business_Partner'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Channel(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Segment(data)


