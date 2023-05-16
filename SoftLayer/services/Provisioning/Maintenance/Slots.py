# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Maintenance_Slots(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Maintenance_Slots'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Slots':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Slots import Slots
        return Slots(data)


