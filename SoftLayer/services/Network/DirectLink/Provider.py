# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_DirectLink_Provider(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_DirectLink_Provider'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_Provider':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.Provider import Provider
        return Provider(data)


