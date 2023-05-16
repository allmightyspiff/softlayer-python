# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def connectPrivateEndpointService(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'connectPrivateEndpointService',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def disconnectPrivateEndpointService(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'disconnectPrivateEndpointService',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network import Network
        return SL_Network(data)

# This file was automatically generated with tools/generateTypes.py
    def isConnectedToPrivateEndpointService(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isConnectedToPrivateEndpointService',
            
        )
        
        return data


