# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Pod(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Pod'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Network_Pod]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Pod import Pod
        return Pod(data)


    def getCapabilities(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getCapabilities',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Pod':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Pod import Pod
        return Pod(data)


    def listCapabilities(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'listCapabilities',
            
        )
        
        return data


