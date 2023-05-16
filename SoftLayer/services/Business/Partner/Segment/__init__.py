# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Business_Partner_Segment(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Business_Partner_Segment'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Segment':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Segment import Segment
        return Segment(data)


