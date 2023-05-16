# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Monitoring_Robot(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Monitoring_Robot'
        self.client = client

    def checkConnection(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'checkConnection',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Monitoring_Robot':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Monitoring.Robot import Robot
        return Robot(data)


