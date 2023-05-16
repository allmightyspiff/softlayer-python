# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_DirectLink_ServiceType(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_DirectLink_ServiceType'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_ServiceType':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.ServiceType import ServiceType
        return ServiceType(data)


