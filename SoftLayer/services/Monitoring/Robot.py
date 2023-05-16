# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Monitoring_Robot(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Monitoring_Robot'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def checkConnection(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'checkConnection',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Monitoring_Robot':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Monitoring.Robot import Robot
        return SL_Robot(data)


