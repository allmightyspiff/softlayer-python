# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Business_Partner_Channel(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Business_Partner_Channel'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Channel':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Channel import Channel
        return Channel(data)


