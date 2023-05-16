# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Auxiliary_Marketing_Event(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Auxiliary_Marketing_Event'
        self.client = client

    def getMarketingEvents(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Auxiliary_Marketing_Event]':

        data = self.client.call(
            self.service,
            'getMarketingEvents',
            mask=objectMask
        )
        from SoftLayer.datatypes.Auxiliary.Marketing.Event import Event
        return Event(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Auxiliary_Marketing_Event':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Auxiliary.Marketing.Event import Event
        return Event(data)


