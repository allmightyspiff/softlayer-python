# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Auxiliary_Network_Status(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Auxiliary_Network_Status'
        self.client = client

    def getNetworkStatus(
        self,
        target: enum
    ) -> 'list[SoftLayer_Container_Auxiliary_Network_Status_Reading]':

        data = self.client.call(
            self.service,
            'getNetworkStatus',
            target
        )
        from SoftLayer.datatypes.Container.Auxiliary.Network.Status.Reading import Reading
        return Reading(data)


