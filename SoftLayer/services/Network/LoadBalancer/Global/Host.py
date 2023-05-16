# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LoadBalancer_Global_Host(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LoadBalancer_Global_Host'
        self.client = client

    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_Global_Host':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Host import Host
        return Host(data)


    def getLoadBalancerAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_Global_Account':

        data = self.client.call(
            self.service,
            'getLoadBalancerAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Account import Account
        return Account(data)


