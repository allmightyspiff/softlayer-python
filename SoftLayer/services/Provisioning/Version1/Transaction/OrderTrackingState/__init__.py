# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState'
        self.client = client

    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Version1_Transaction_OrderTrackingState':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Version1.Transaction.OrderTrackingState import OrderTrackingState
        return OrderTrackingState(data)


